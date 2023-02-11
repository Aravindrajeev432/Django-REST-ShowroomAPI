from rest_framework import serializers
from django.core.serializers import serialize

from cars.models import Cars, DisplayCars, DisplayCarImages
from account.models import Account
from cars.serializers import ColourSerializer, FuelTypeSerializer,\
    GearTypeSerializer
import json


class CarSerialoizer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = '__all__'


class GetCustomersSerializer(serializers.ModelSerializer):
    usercar = CarSerialoizer(many=True, read_only=True)

    class Meta:
        model = Account
        fields = ('username', 'id', 'usercar')
        # depth = 1


class CarAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = '__all__'


class DisplayCarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisplayCarImages
        fields = '__all__'


class DisplayCarsImageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisplayCarImages
        fields = "__all__"


class DisplayCarImageSerializer(serializers.ModelSerializer):
    # images=serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='images-list')
    class Meta:
        model = DisplayCarImages
        fields = ['image']


class DisplayCarsSerializer(serializers.ModelSerializer):
    colour = ColourSerializer(many=True, read_only=True)
    gear_type = GearTypeSerializer(many=True, read_only=True)
    fuel_type = FuelTypeSerializer(many=True, read_only=True)
    carimg = DisplayCarImageSerializer(many=True, read_only=True)

    class Meta:
        model = DisplayCars
        fields = '__all__'

    def create(self, validated_data):
        request = self.context['request']
        print(request.data)

        colour = request.data.get('colour')
        validated_data['colour'] = colour

        gear_type = request.data.get('gear_type')
        validated_data['gear_type'] = gear_type

        fuel_type = request.data.get('fuel_type')
        validated_data['fuel_type'] = fuel_type

        instance = super().create(validated_data)
        return instance


class DisplayCarsDetailsRelationsSerializer(serializers.Serializer):
    colours = ColourSerializer()
    gear_types = GearTypeSerializer()
    fuel_types = FuelTypeSerializer()


class FrontDeskDashboardSerializer(serializers.Serializer):
    pending_request = serializers.CharField(max_length=200)
    new_service_request = serializers.CharField(max_length=200)
    online_advisors = serializers.CharField(max_length=200)
