from dataclasses import field
from rest_framework.serializers import ModelSerializer
from . models import ZakatTable


class ZakatTableSerializer(ModelSerializer):
    class Meta:
        model = ZakatTable
        fields = '__all__'