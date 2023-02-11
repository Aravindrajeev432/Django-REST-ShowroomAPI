from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters

from django_auto_prefetching import AutoPrefetchViewSetMixin

from rest_framework import generics

from cars.models import CarParts, UniPartNumbers, Cars

from .pagination import PartsPagination
from .serializers import CarPartsSerializer, UniCarPartsSerializer,CarPartUpdateSerializer


# Create your views here.
class AddParts(AutoPrefetchViewSetMixin, generics.ListCreateAPIView):
    serializer_class = CarPartsSerializer
    queryset = CarParts.objects.all()
    pagination_class = PartsPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['unique_part_name']


class UniCarPartNumbers(generics.ListAPIView):
    serializer_class = UniCarPartsSerializer
    queryset = UniPartNumbers.objects.all()


class PartUpdator(AutoPrefetchViewSetMixin, generics.RetrieveUpdateAPIView):
    serializer_class = CarPartUpdateSerializer
    queryset = CarParts.objects.all()
    lookup_field = 'pk'
