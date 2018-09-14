from rest_framework.serializers import ModelSerializer

from .models import *


class CharityLotSerializer(ModelSerializer):
    class Meta:
        model = CharityLot
        fields = '__all__'
