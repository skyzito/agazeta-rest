from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from rest_framework.throttling import UserRateThrottle
from .permissions import IsOwnerOrReadOnly, IsOwner
from .serializers import UserSerializer, TobTokenSerializer, TobTokenSerializerVersion1, MatchSerializer, CardPlayedSerializer
from .models import TobToken, Match, CardPlayed

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    throttle_classes = (UserRateThrottle,)
    permission_classes = (permissions.IsAdminUser, IsOwner,)
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class TobTokenViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    throttle_classes = (UserRateThrottle,)
    permission_classes = (permissions.IsAdminUser, IsOwner,)
    queryset = TobToken.objects.all()
    serializer_class = TobTokenSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.request.version == 'v1':
            return TobTokenSerializerVersion1
        return TobTokenSerializer


class MatchViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    throttle_classes = (UserRateThrottle,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    queryset = Match.objects.all()
    serializer_class = MatchSerializer


class CardPlayedViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    throttle_classes = (UserRateThrottle,)
    permission_classes = (permissions.IsAdminUser, IsOwnerOrReadOnly,)
    queryset = CardPlayed.objects.all()
    serializer_class = CardPlayedSerializer