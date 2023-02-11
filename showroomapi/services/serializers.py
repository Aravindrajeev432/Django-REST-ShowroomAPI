from rest_framework import serializers

from account.models import Account
from cars.models import Cars
from rest_framework.serializers import ModelSerializer

from .models import Services, ServiceInfo, BayDetails, ServiceHistory


class ServiceUserSerializer(serializers.ModelSerializer):
    class Meta:
        model= Account
        fields=['username','phone_number']

class ServiceCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields= ['model_name','model_year']

class SerivesSerializer(serializers.ModelSerializer):
    user = ServiceUserSerializer()
    advisor =ServiceUserSerializer()
    car = ServiceCarSerializer()
    class Meta:
        model = Services
        fields = '__all__'

class ServiceAssignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'


class ServiceInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceInfo
        fields = '__all__'


# class CarsServiceDistinct(serializers.Serializer):
#     universal_car_number=

class UniCarNumSerializer(serializers.ModelSerializer):
    label = serializers.CharField(source='universal_car_number')
    value = serializers.CharField(source='universal_car_number')

    class Meta:
        model = Cars
        # fields = ('universal_car_number',)
        fields = ['value', 'label']
        # read_only_fields = ('universal_car_number',)


class BayDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = BayDetails
        fields = '__all__'






