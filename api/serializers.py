from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

from .models import *


class CharityLotSerializer(ModelSerializer):
    class Meta:
        model = CharityLot
        fields = '__all__'

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name')
