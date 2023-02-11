from rest_framework import serializers
from cars.models import CarParts, UniPartNumbers, UniPartNumbers, Cars


class UniPartNumberSerializer(serializers.ModelSerializer):

    value = serializers.CharField(source='id')
    label = serializers.CharField(source='universal_car_part_number')

    class Meta:
        model = UniPartNumbers
        fields = ['value', 'label']


class CarPartsSerializer(serializers.ModelSerializer):
    compatible_cars = UniPartNumberSerializer(many=True, read_only=True)

    class Meta:
        model = CarParts
        fields = '__all__'

    def create(self,validated_data):
        request = self.context['request']
        compatible_cars = request.data.get('compatible_cars')
        validated_data['compatible_cars'] = compatible_cars

        instance = super().create(validated_data)
        return instance

class UniCarPartsSerializer(serializers.ModelSerializer):
    value = serializers.CharField(source='id')
    label = serializers.CharField(source='universal_car_part_number')

    class Meta:
        model = UniPartNumbers
        fields = ['value', 'label']

class CarPartUpdateSerializer(serializers.ModelSerializer):
    # compatible_cars = UniCarPartsSerializer(many=True)

    class Meta:
        model = CarParts
        fields = '__all__'

