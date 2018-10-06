from django.shortcuts import render
from django.contrib.auth import login

from rest_framework import generics, views
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer

from knox.auth import TokenAuthentication
from knox.views import LoginView as KnoxLoginView

from .serializers import *
import api.utils as utils
from mailer.actions import send_password

class CharityLotsList(generics.ListAPIView):
    permission_classes = (AllowAny,)

    queryset = CharityLot.objects.all()
    serializer_class = CharityLotSerializer


class CharityBidsList(views.APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        queryset = CharityBid.objects.filter(user=request.user)
        serializer = CharityBidSerializer(queryset, many=True)
        return Response(serializer.data)


class UserInfoView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class UserResetPassword(views.APIView):
    def post(self, request):
        username = request.data["username"];
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({ "status": "user_not_found" })

        new_password = utils.generate_password()
        user.set_password(new_password)
        user.save()

        send_password(user, new_password)
        return Response({ "status": "ok" })


class UserRegisterView(views.APIView):
    def post(self, request):
        username = request.data["username"];
        first_name = request.data["name"];

        new_password = utils.generate_password()
        try:
            user = User.objects.get(username=username)
            user.set_password(new_password)
            user.first_name = first_name
            user.save()
        except User.DoesNotExist:
            user = User.objects.create_user(username, username, new_password)
            user.first_name = first_name
            user.save()

        send_password(user, new_password)
        return Response({ "status": "ok" })


class AuthLoginView(KnoxLoginView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(AuthLoginView, self).post(request, format=None)
