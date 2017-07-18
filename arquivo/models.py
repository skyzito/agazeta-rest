from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    ACCOUNT_TYPE = (
        ('f', 'Free'),
        ('p', 'Paid'),
        ('d', 'Demo'),
        ('c', 'Consultant'),
        ('s', 'Staff')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_type = models.CharField(max_length=30, choices=ACCOUNT_TYPE, default=ACCOUNT_TYPE[0])
    avatar = models.IntegerField(blank=True, null=True)
    partner_sub = models.BooleanField(default=True)
    newsletter_sub = models.BooleanField(default=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

class TobToken(models.Model):
    SERVERS = (
        ('a', 'Americas'),
        ('e', 'Europa'),
        ('c', 'Asia'),
    )
    username = models.CharField(max_length=80)
    token = models.CharField(max_length=80)
    server = models.CharField(max_length=10, choices=SERVERS, default=SERVERS[0])
    is_active = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        unique_together = ['username', 'token']

    def __str__(self):
        return "tob_token [is_active={} server={}]".format(self.is_active, self.server)

    def __repr__(self):
        return "tob_token [id={} username={} is_active={} server={} {}]".format(self.id, self.username, self.is_active, self.server, self.user)

class Match(models.Model):
    match_id = models.IntegerField(unique=True)
    match_mode = models.CharField(max_length=20, blank=False, null=False)
    user = models.ManyToManyField(User)
    date = models.DateField()
    blue_rank = models.IntegerField(blank=True, null=True)
    blue_hero = models.CharField(max_length=30)
    blue_deck = models.CharField(max_length=80,blank=True, null=True)
    red_hero = models.CharField(max_length=30, blank=True)
    red_deck = models.CharField(max_length=80, blank=True, null=True)
    turns_played = models.IntegerField(blank=True, null=True)
    red_starts = models.BooleanField()
    blue_won = models.BooleanField()
    blue_played_cards = models.ManyToManyField('CardPlayed', related_name="blue_played_cards+")
    red_played_cards = models.ManyToManyField('CardPlayed', related_name="red_played_cards+")

    def __str__(self):
        return "archive [matchid={} date={} {} blue={} red={}]".format(self.matchid, self.date, self.user.id, self.hero, self.opponent_hero)

class CardPlayed(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    card = models.CharField(max_length=20)
    turn_played = models.IntegerField()
    is_spawned = models.BooleanField(default=False)

    class Meta:
        ordering = ('match_id',)

    def __str__(self):
        return "card_played [card={} turn_played={} is_spawned={}]".format(self.card, self.turn_played, self.is_spawned)

    def __repr__(self):
        return "card_played [card={} match_id={} turn_played={} is_spawned={}]".format(self.card, self.match.id, self.turn_played, self.is_spawned)
