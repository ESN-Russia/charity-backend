from django.shortcuts import render
from django.contrib.auth import login

from rest_framework import generics, views
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer

from knox.auth import TokenAuthentication
from knox.views import LoginView as KnoxLoginView

from .serializers import *

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


class AuthLoginView(KnoxLoginView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(AuthLoginView, self).post(request, format=None)
