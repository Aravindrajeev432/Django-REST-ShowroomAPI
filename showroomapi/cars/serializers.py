import code
from pyexpat import model

from rest_framework import serializers

from .models import Cars, Colours, FuelType, GearType, DisplayCars,DisplayCarImages


def power_validator(power):
    print("power_validator")
    p = int(power)
    if p < 50 or p > 300:
        raise serializers.ValidationError("power_error", code="power_error")
    return power


def price_validator(price):
    print("price_validator")
    p = int(price)
    if p < 100000 or p > 10000000:
        raise serializers.ValidationError("price_error", code="price_error")
    return price


def wheel_base_validator(wheel):
    wheel = int(wheel)
    if wheel < 15 or wheel > 25:
        raise serializers.ValidationError("wheel_error", code="wheel_base_error")
    return wheel


class SaveStockCarSerializer(serializers.ModelSerializer):
    engine_power = serializers.CharField(validators=[power_validator])
    price = serializers.CharField(validators=[price_validator])
    wheel_base = serializers.CharField(validators=[wheel_base_validator])

    def validate(self, data):
        print("--")
        print(data)
        # if(data['power']=="344"):
        #     print(data['power'])
        #     raise serializers.ValidationError("power error")
        # raise serializers.ValidationError("power error")
        return data

    class Meta:
        model = Cars
        fields = '__all__'


class CheckEngineNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = ['model_name', 'engine_number']


class ColourSerializer(serializers.ModelSerializer):
    label = serializers.CharField(source='colour_name')
    value = serializers.CharField(source='id')

    class Meta:
        model = Colours
        fields = ['value', 'label']


class FuelTypeSerializer(serializers.ModelSerializer):
    label = serializers.CharField(source='fuel_type')
    value = serializers.CharField(source='id')

    class Meta:
        model = FuelType
        fields = ['value', 'label']


class GearTypeSerializer(serializers.ModelSerializer):
    label = serializers.CharField(source='gear_type')
    value = serializers.CharField(source='id')

    class Meta:
        model = GearType
        fields = ['value', 'label']

class GearTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GearType
        fields = "__all__"

class CustomerColourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colours
        fields = "__all__"

class DisplayCarImageSerializer(serializers.ModelSerializer):
    # images=serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='images-list')
    class Meta:
        model = DisplayCarImages
        fields = ['image']
class DisplayCarsSerializer(serializers.ModelSerializer):
    colour = ColourSerializer(many=True)
    gear_type = GearTypeSerializer(many=True)
    fuel_type = FuelTypeSerializer(many=True)
    carimg = DisplayCarImageSerializer(many=True, read_only=True)
    class Meta:
        model = DisplayCars
        fields = '__all__'

class DisplayCarsModel_nameSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisplayCars
        fields = ['model_name']
class DisplayCarTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisplayCars
        fields = ['type']


class TestSerializer(serializers.Serializer):
    colour = serializers.CharField(source="colour.colour_name")
