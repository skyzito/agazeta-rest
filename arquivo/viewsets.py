from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from rest_framework.throttling import UserRateThrottle
from .permissions import IsOwnerOrReadOnly, IsOwner
from .serializers import UserSerializer, TobTokenSerializer, TobTokenSerializerVersion1, MatchSerializer, CardPlayedSerializer
from .models import TobToken, Match, CardPlayed

class UserViewSet(viewsets.ModelViewSet):
    """
    User set
    ---
    retrieve:
        Return a user instance.

    list:
        Return all users, ordered by most recently joined.

    create:
        Create a new user.

    delete:
        Remove an existing user.

    partial_update:
        Update one or more fields on an existing user.

    update:
        Update a user.
    """
    throttle_classes = (UserRateThrottle,)
    permission_classes = (permissions.IsAdminUser, IsOwner,)
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class TobTokenViewSet(viewsets.ModelViewSet):
    """
    Track-o-Bot token resource
    ---
    retrieve:
        Return a Track-o-Bot token instance.

    list:
        Return all Track-o-Bot tokens that you have access.

    create:
        Create a new Track-o-Bot token entry in the database.

    delete:
        Remove an existing Track-o-Bot token.

    partial_update:
        Update one or more fields on an existing Track-o-Bot token.

    update:
        Update a Track-o-Bot token.
    """
    throttle_classes = (UserRateThrottle,)
    permission_classes = (permissions.IsAdminUser, IsOwner,)
    queryset = TobToken.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.request.version == 'v1':
            return TobTokenSerializerVersion1
        return TobTokenSerializer


class MatchViewSet(viewsets.ModelViewSet):
    """
    Match resource
    ---
    retrieve:
        Return a match instance.

    list:
        Return all match instances.

    create:
        Create a new Track-o-Bot token entry in the database.

    delete:
        Remove an existing Track-o-Bot token.

    partial_update:
        Update one or more fields on an existing Track-o-Bot token.

    update:
        Update a Track-o-Bot token.
    """
    throttle_classes = (UserRateThrottle,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

class CardPlayedViewSet(viewsets.ModelViewSet):
    """
    Card Played on matchs
    ---
    retrieve:
        Return a card played in a match.

    list:
        Return all cards of a given match.

    create:
        Create a new card to add to a player in a match.

    delete:
        Remove an existing card from database.

    partial_update:
        Update one or more fields on an existing played card.

    update:
        Update a played card.
    """
    throttle_classes = (UserRateThrottle,)
    permission_classes = (permissions.IsAdminUser, IsOwnerOrReadOnly,)
    queryset = CardPlayed.objects.all()
    serializer_class = CardPlayedSerializer