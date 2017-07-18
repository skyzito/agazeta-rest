from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from rest_framework.throttling import UserRateThrottle
from .permissions import IsOwnerOrReadOnly, IsOwner

def account_profile(request):
	pass

def analytics(request):
    pass