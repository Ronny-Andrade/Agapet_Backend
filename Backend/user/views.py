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
from .serializers import UserSerializer, RegisterSerializer, UserUpdateSerializer
# Models
from .models import User
from django.conf import settings
from django.core.mail import send_mail


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


class EmailAPI(APIView):
    def get(self, request):
        subject = self.request.GET.get('subject')
        txt_ = self.request.GET.get('text')
        html_ = self.request.GET.get('html')
        recipient_list = self.request.GET.get('recipient_list')
        from_email = settings.DEFAULT_FROM_EMAIL

        if subject is None and txt_ is None and html_ is None and recipient_list is None:
            return Response({'msg': 'There must be a subject, a recipient list, and either HTML or Text.'}, status=200)
        elif html_ is not None and txt_ is not None:
            return Response({'msg': 'You can either use HTML or Text.'}, status=200)
        elif html_ is None and txt_ is None:
            return Response({'msg': 'Either HTML or Text is required.'}, status=200)
        elif recipient_list is None:
            return Response({'msg': 'Recipient List required.'}, status=200)
        elif subject is None:
            return Response({'msg': 'Subject required.'}, status=200)
        else:
            sent_mail = send_mail(
                subject,
                txt_,
                from_email,
                recipient_list.split(','),
                html_message=html_,
                fail_silently=False,
            )
            return Response({'msg': sent_mail}, status=200)

