# from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from .models import Group, Message
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from .serializers import (
    UserSerializer,
    GroupSerializer,
    MessageSerializer,
    UserCreateSerializer,
)

from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.views import APIView


class UserCreateView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    authentication_classes = [TokenAuthentication]
    serializer_class = UserCreateSerializer


class UserUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAdminUser]
    authentication_classes = [TokenAuthentication]
    serializer_class = UserCreateSerializer


class GroupCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupListView(generics.ListAPIView):
    queryset = Group.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = GroupSerializer


class GroupMemberAddView(generics.UpdateAPIView):
    queryset = Group.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = GroupSerializer


class MessageCreateView(generics.CreateAPIView):
    queryset = Message.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = MessageSerializer


class MessageListView(generics.ListAPIView):
    queryset = Message.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = MessageSerializer
