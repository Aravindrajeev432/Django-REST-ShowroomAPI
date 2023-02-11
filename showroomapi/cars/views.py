from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import json
from rest_framework import generics
from django.db.models import Q
import itertools
from .models import Cars, Colours, GearType, FuelType, DisplayCars
from .serializers import SaveStockCarSerializer, CheckEngineNumberSerializer, ColourSerializer, GearTypeSerializer, \
    FuelTypeSerializer, DisplayCarsSerializer, DisplayCarsModel_nameSerializer, DisplayCarTypesSerializer, \
    GearTypesSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django_auto_prefetching import AutoPrefetchViewSetMixin

# Create your views here.
class AddNewCar(APIView):
    # queryset = Cars.objects.all()
    # serializer_class = StockCarSerializer
    def post(self, request):
        body = request.data
        print(body)
        print(type(body))
        body['verified_by'] = request.user.username
        serializer = SaveStockCarSerializer(data=body)
        if serializer.is_valid():
            print("valid")
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            print("invalid")
            data = {"errorText": serializer.errors}
            return Response(status=status.HTTP_400_BAD_REQUEST, data=data)
        print(serializer.data)
        return Response(status=status.HTTP_201_CREATED)


class CheckEngineNumber(APIView):
    def get(self, request, engine_number):

        # car = Cars.objects.get(engine_number=engine_number)
        if Cars.objects.filter(engine_number=engine_number).exists():
            # print(car)

            car = Cars.objects.get(engine_number=engine_number)
            print(car.user)
            if car.user is not None:
                return Response(status=status.HTTP_409_CONFLICT)
            data = {"id": car.id,
                    "model_name": car.model_name,
                    "model_year": car.model_year,
                    "colour": car.colour,
                    "gear_type": car.gear_type,
                    "fuel_type": car.fuel_type,
                    "seat_capacity": car.seat_capacity,
                    }
            return Response(data=data, status=status.HTTP_200_OK)

            # serializerObj = CheckEngineNumberSerializer(data=car,many=True)
            # print(serializerObj.data)
            # if serializerObj.is_valid():
            #
            #     return Response(serializerObj.data,status=status.HTTP_200_OK)
            # else:
            #     return Response(serializerObj.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(status=status.HTTP_200_OK)


# class GetFilterData(generics.ListAPIView):
#
#         queryset = DisplayCars.objects.values('model_name','type').distinct()
#         serializer_class = DisplayCarsModel_nameSerializer

class GetFilterData(APIView):
    def get(self, request):
        gear_types = GearType.objects.values('gear_type')
        gear_typeSerializerobj = GearTypesSerializer(gear_types, many=True)

        types_querysets = DisplayCars.objects.values('type').distinct()
        types_serializerobj = DisplayCarTypesSerializer(types_querysets, many=True)

        types = []
        gear_types = []

        for i in gear_typeSerializerobj.data:
            for key, value in i.items():
                gear_types.append(value)

        for i in types_serializerobj.data:
            for key, value in i.items():
                types.append(value)

        data = {

            "types": types,
            "gear_types": gear_types,
            "seat_capacity": ["5", "6", "7"]
        }
        return Response(data=data, status=status.HTTP_200_OK)


class GetDisplayCarsDetails(APIView):
    def get(self, request):
        colors = Colours.objects.all()
        print(colors)
        gear_types = GearType.objects.all()
        fuel_types = FuelType.objects.all()
        colourobj = ColourSerializer(colors, many=True)
        gear_typesobj = GearTypeSerializer(gear_types, many=True)
        fuel_typesobj = FuelTypeSerializer(fuel_types, many=True)

        data = {
            "colours": colourobj.data,
            "gear_types": gear_typesobj.data,
            "fuel_types": fuel_typesobj.data,
        }
        return Response(data, status=status.HTTP_200_OK)


class UserDisplayCars(AutoPrefetchViewSetMixin,generics.ListAPIView):
    queryset = DisplayCars.objects.filter(Q(is_active=True))
    serializer_class = DisplayCarsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['type', 'gear_type', 'seat_capacity']
