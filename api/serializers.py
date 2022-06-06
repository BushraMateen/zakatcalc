from dataclasses import field
from rest_framework.serializers import ModelSerializer
from . models import ZakatTable
from . models import ZakatDetails


class ZakatTableSerializer(ModelSerializer):
    class Meta:
        model = ZakatTable
        fields = '__all__'


class  ZakatDetailsSerializer(ModelSerializer):
    class Meta:
        model =  ZakatDetails
        fields = '__all__'