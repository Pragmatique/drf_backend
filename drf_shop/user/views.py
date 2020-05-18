from django.shortcuts import render
from rest_framework import viewsets, views
from rest_framework.generics import GenericAPIView, RetrieveAPIView
from rest_framework.mixins import UpdateModelMixin, CreateModelMixin, ListModelMixin
# from rest_framework.permissions import AllowAny
from rest_framework import permissions

from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.http import HttpResponse, HttpResponseRedirect

import smtplib
from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from .models import MyUser
from .serializers import MyUserSerializer, SimpleUserSerializer
from .permissions import IsOwnerOrAdmin, IsAdmin, IsPostOrIsAuthenticated


class UserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
    permission_classes = [IsPostOrIsAuthenticated, IsOwnerOrAdmin]

    def post(self, request, *args, **kwargs):
        print('begin post')
        user = self.create(request, *args, **kwargs)
        print(user.data['email'], user.data['id'])
        mail_verification_send(user.data['email'], user.data['id'])
        return user


# GenericAPIView, CreateModelMixin, UpdateModelMixin
# class MyUserViewSet(RetrieveAPIView):
#     queryset = MyUser.objects.all()
#     serializer_class = MyUserSerializer
#     permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]
#
#     def patch(self, request, *args, **kwargs):
#         return self.patch(request, *args, **kwargs)


class UserCreateView(GenericAPIView, CreateModelMixin):
    queryset = MyUser.objects.all()
    serializer_class = SimpleUserSerializer
    # permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]


class UserPartialUpdateView(GenericAPIView, UpdateModelMixin):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
    permission_classes = [IsPostOrIsAuthenticated, IsOwnerOrAdmin]

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


def mail_verification_send(mail, user_id):
    print('begin')
    msg = MIMEMultipart()
    # Sender
    msg['From'] = 'test@test.com'
    # Receiver
    msg['To'] = mail
    msg['Subject'] = 'Verification email on localhost'
    message = 'http://127.0.0.1:8000/api/users/mail-verification/{}/'.format(user_id)
    msg.attach(MIMEText(message))

    mailserver = smtplib.SMTP('localhost', 1025)
    mailserver.sendmail('test@test.com', mail, msg.as_string())
    mailserver.quit()
    print('end')


def activate_account(request, pk):
    print(request, pk)
    try:
        # pk = force_bytes(urlsafe_base64_decode(pk))
        print('got pk', pk)
        user = MyUser.objects.get(pk=pk)
        print('got user')
    except Exception:
        return HttpResponse(status=400)

    if user:
        user.is_active = True
        user.save()
        return HttpResponseRedirect('http://localhost:8080/login')
    return HttpResponse(status=400)

