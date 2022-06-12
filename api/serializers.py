from dataclasses import field
from rest_framework.serializers import ModelSerializer
from . models import ZakatTable
from . models import ZakatDetails
from . models import Usermapping


class ZakatTableSerializer(ModelSerializer):
    class Meta:
        model = ZakatTable
        fields = '__all__'


class  ZakatDetailsSerializer(ModelSerializer):
    class Meta:
        model =  ZakatDetails
        fields = '__all__'

class  UsermappingSerializer(ModelSerializer):
    class Meta:
        model =  Usermapping
        fields = '__all__'