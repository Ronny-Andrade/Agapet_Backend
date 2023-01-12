# Native
from django.shortcuts import render
# Django Rest Framework
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
import jwt, datetime
# Serializers
from .serializers import UserSerializer, RegisterSerializer, UserUpdateSerializer, ImageUpdateSerializer
# Models
from .models import User
# Imagen base64
import base64
from django.core.files.base import ContentFile

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors ,status= status.HTTP_400_BAD_REQUEST)


class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class UserView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        serializar = UserSerializer(request.user)
        return Response(serializar.data)
    


class Userupdate(APIView):
    def put(self, request):
        user = User.objects.get(iduser=request.user.iduser)
        serializer = UserUpdateSerializer(instance=user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ImageUserupdate(APIView):
    def put(self, request):
        user = User.objects.get(iduser=request.user.iduser)
        serializer = ImageUpdateSerializer(instance=user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


