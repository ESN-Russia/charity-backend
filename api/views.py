from django.shortcuts import render
from django.contrib.auth import login

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer

from knox.auth import TokenAuthentication
from knox.views import LoginView as KnoxLoginView

from .serializers import *

class CharityLotsList(generics.ListAPIView):
    # permission_classes = (AllowAny,)

    queryset = CharityLot.objects.all()
    serializer_class = CharityLotSerializer


class AuthLoginView(KnoxLoginView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(AuthLoginView, self).post(request, format=None)
