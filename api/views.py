from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import *

class CharityLotsList(generics.ListAPIView):
    queryset = CharityLot.objects.all()
    serializer_class = CharityLotSerializer
