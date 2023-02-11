from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
from django.db.models import Q
from django.http import HttpResponse

from django_auto_prefetching import AutoPrefetchViewSetMixin

# Create your views here.
from .models import Services, ServiceInfo, BayDetails
from .serializers import SerivesSerializer, UniCarNumSerializer, ServiceInfoSerializer, \
    BayDetailsSerializer, ServiceAssignSerializer
from cars.models import Cars
from .pagination import ServiceInfoPagination

from django.template.loader import get_template
from xhtml2pdf import pisa

import datetime
from dateutil import relativedelta


class AllServices(AutoPrefetchViewSetMixin, generics.ListAPIView):
    serializer_class = SerivesSerializer
    queryset = Services.objects.all()


class GetUniCarNum(AutoPrefetchViewSetMixin, APIView):
    def get(self, request):
        # universal car number
        uni_car_num = Cars.objects.values('universal_car_number').distinct('universal_car_number').filter(
            ~Q(universal_car_number__in=ServiceInfo.objects.all().values_list('universal_car_number', flat=True)))

        serializerobj = UniCarNumSerializer(uni_car_num, many=True)

        # the response is value ,label format for react select package
        return Response(data=serializerobj.data, status=status.HTTP_200_OK)


# from car models all universal car number
class GetDistinctUniCarNum(generics.ListAPIView):
    serializer_class = UniCarNumSerializer
    queryset = Cars.objects.values('universal_car_number').distinct('universal_car_number')


class AddServiceInfo(generics.CreateAPIView):
    serializer_class = ServiceInfoSerializer
    queryset = ServiceInfo.objects.all()


class ShowServiceinfo(generics.ListAPIView):
    pagination_class = ServiceInfoPagination
    serializer_class = ServiceInfoSerializer
    queryset = ServiceInfo.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['universal_car_number']


class RequestService(APIView):
    def post(self, request):
        # {'car':'car_id'}
        print(request.data)
        try:
            car = Cars.objects.get(id=request.data['car'])
            service_check = Services.objects.filter(Q(car=car) & ~Q(status='finished'))
            if not service_check.exists():
                print("Okay to accept the request")

                try:
                    service_info = ServiceInfo.objects.get(universal_car_number=car.universal_car_number)


                except ServiceInfo.DoesNotExist:
                    return Response(status=status.HTTP_404_NOT_FOUND)
                number_of_services = Services.objects.filter(car=car).count()

                if number_of_services < service_info.number_of_free_services:
                    is_free = True
                else:
                    is_free = False

                service = Services.objects.create(car=car, status='requested', user=request.user, is_free=is_free)
                service.save()

                return Response(status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_409_CONFLICT)
        except Cars.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(status=status.HTTP_201_CREATED)

    def get(self, request):
        return Response(status=status.HTTP_200_OK)


class Service(APIView):
    def get(self, request, service_status):
        print(service_status)
        s = Services.objects.filter(status=service_status)
        print(s)
        serializerobj = SerivesSerializer(s, many=True)
        return Response(serializerobj.data, status=status.HTTP_200_OK)


class ServiceAssignAdvisor(generics.UpdateAPIView):
    serializer_class = ServiceAssignSerializer
    queryset = Services.objects.all()
    lookup_field = 'id'


class GetFreeBays(generics.ListAPIView):
    serializer_class = BayDetailsSerializer
    queryset = BayDetails.objects.filter(status='free')


# class ServiceCompleter(generics.UpdateAPIView):
#     serializer_class =
#     queryset = Services.objects.all()
#     lookup_field = 'pk'

class ServiceCompleter(APIView):
    def post(self,request):
        print(request.data['service_id'])
        print(request.data['make_complete'])
        if request.data['make_complete']:
            Services.objects.filter(id=request.data['service_id']).update(status='finished')
        return Response(status=status.HTTP_202_ACCEPTED)



def billgenerator(request, id):
    print(id)
    try:
        service = Services.objects.get(id=id)

        total = 0
        for t in service.service_log.all():
            total = t.amount

        context = {
            'service': service,
            'parts': service.parts_used.all(),
            'total': total

        }
    except Services.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    template_path = 'pdf/invoice.html'

    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposition'] = 'filename="invoice.pdf"'

    template = get_template(template_path)

    html = template.render(context)
    pisa_status = pisa.CreatePDF(
        html, dest=response
    )
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
