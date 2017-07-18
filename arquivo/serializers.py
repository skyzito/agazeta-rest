from django.contrib.auth.models import User
from .models import Profile, TobToken, Match, CardPlayed
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    # A field from the user's profile:
    avatar = serializers.URLField(source='profile.avatar', allow_blank=True)
    partner_sub = serializers.URLField(source='profile.partner_sub', allow_blank=True)
    newsletter_sub = serializers.URLField(source='profile.newsletter_sub', allow_blank=True)
    account_type = serializers.URLField(source='profile.account_type', allow_blank=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'avatar', 'account_type', 'partner_sub', 'newsletter_sub')

    def create(self, validated_data):
        profile_data = validated_data.pop('profile', None)
        user = super(UserSerializer, self).create(validated_data)
        self.update_or_create_profile(user, profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', None)
        self.update_or_create_profile(instance, profile_data)
        return super(UserSerializer, self).update(instance, validated_data)

    def update_or_create_profile(self, user, profile_data):
        # This always creates a Profile if the User is missing one;
        # change the logic here if that's not right for your app
        Profile.objects.update_or_create(user=user, defaults=profile_data)

class TobTokenSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = TobToken
        fields = ('username', 'token', 'server', 'is_active', 'user')

class TobTokenSerializerVersion1(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TobToken
        fields = ('username', 'token', 'is_active')


class CardPlayedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CardPlayed
        fields = ('match', 'card', 'turn_played', 'is_spawned')

class MatchSerializer(serializers.ModelSerializer):

    blue_played_cards  = CardPlayedSerializer(many=True)
    red_played_cards = CardPlayedSerializer(many=True)

    class Meta:
        model = Match
        fields = ('match_id', 'match_mode', 'date', 'blue_rank', 'blue_hero',
                  'blue_deck', 'red_hero', 'red_deck', 'turns_played', 'red_starts', 'red_starts',
                  'blue_won', 'blue_played_cards', 'red_played_cards')
