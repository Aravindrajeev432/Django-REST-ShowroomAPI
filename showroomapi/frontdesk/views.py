import itertools

from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.renderers import JSONRenderer


from .serializers import GetCustomersSerializer, CarSerialoizer, CarAvailabilitySerializer, DisplayCarsSerializer, \
    DisplayCarsDetailsRelationsSerializer,DisplayCarsImageCreateSerializer,FrontDeskDashboardSerializer
from .custom_serializer import Dashboard

from account.models import Account
from cars.models import Cars, DisplayCars,DisplayCarImages
from advisor.models import AdvisorsOnline
from services.models import Services
from .models import CarEnquiresmodel
from .paginations import DisplayCarsPagination
from account.custom_permissions import IsFrontDesk
from django.db.models import Q



# Create your views here.


class CreateCustomer(APIView):
    def get(self, request):
        return Response(200)

    def post(self, request):
        body = request.data
        print(body)
        if Account.objects.filter(phone_number=body['phone_number']).exists():
            data = {'message': "phone number already exists"}
            return Response(data=data, status=status.HTTP_409_CONFLICT)
        elif Account.objects.filter(email=body['email']).exists():
            data = {'message': "email already exists"}
            return Response(data=data, status=status.HTTP_409_CONFLICT)
        elif Account.objects.filter(username=body['username']).exists():
            data = {'message': "username already exists"}
            return Response(data=data, status=status.HTTP_409_CONFLICT)
        else:

            user = Account.objects.create_customer(username=body['username'], email=body['email'],
                                                   phone_number=body['phone_number'], password=body['phone_number'])

            car = Cars.objects.get(engine_number=body['engine_number'])
            car.user = user
            car.save()
            data = {'message': "customer created successfully"}
        return Response(status=status.HTTP_201_CREATED)


class UpdateCustomer(APIView):
    def post(self, request):
        body = request.data
        user = Account.objects.get(id=body['user_id'])
        car = Cars.objects.get(engine_number=body['engine_number'])
        print(user)
        print(car)
        car.user = user
        car.save()
        return Response(status=status.HTTP_202_ACCEPTED)


class GetCustomers(generics.ListAPIView):
    # customeers = Account.objects.filter(is_customers=True)
    model = Account
    serializer_class = GetCustomersSerializer
    queryset = Account.objects.filter(is_customer=True)


# class GetCustomers(APIView):
#     def get(self, request):
#         car = Cars.objects.filter(Q(is_deleted=False))
#         # print(car)
#         serializerObj = CarSerialoizer(car, many=True)
#         print(serializerObj.data)
#         # if serializerObj.is_valid():
#         #     print(serializerObj.data)
#         # else:
#         #     print(serializerObj.errors)
#         return Response(serializerObj.data, 200)

class CarAvailabilityPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class CarAvilabilty(generics.ListAPIView):
    # permission_classes = [IsFrontDesk]
    def __init__(self, *args, **kwargs):
        # q = ProductOrder.objects.values('Category').distinct()
        test = Cars.objects.values('model_name').distinct()


    model = Cars
    serializer_class = CarAvailabilitySerializer
    queryset = Cars.objects.filter(Q(is_deleted=False) & Q(user=None))
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['model_name', 'model_year', 'type', 'gear_type', 'colour']
    pagination_class = CarAvailabilityPagination


class GetFilterData(APIView):

    def get(self, request):
        model_names = Cars.objects.values('model_name').distinct(),
        model_years = Cars.objects.values('model_year').distinct(),

        model_names = list(itertools.chain(*model_names))
        model_years = list(itertools.chain(*model_years))

        model_names_list = []
        model_years_list = []

        for i in model_names:
            model_names_list.append(i["model_name"])
        for i in model_years:
            model_years_list.append(i["model_year"])

        data = {"model_names": model_names_list,
                "model_years": model_years_list,
                "types": ['Sedan', 'SUV', 'Hatchback'],
                "gear_types": ['DCT', 'AMT', 'manual'],
                "colours": ['Red', 'Green', 'Blue', 'White']
                }

        return Response(data, status=status.HTTP_200_OK)


class AddDisplayCars(generics.ListCreateAPIView):


    parser_classes = [JSONParser]
    pagination_class = DisplayCarsPagination
    queryset = DisplayCars.objects.filter(~Q(is_deleted=True)).prefetch_related('colour','gear_type','fuel_type').order_by('-id').all()

    serializer_class = DisplayCarsSerializer


class TestDisplayCars(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        print(request.data)
        form_data = request.data
        print(form_data)

        #
        # f1 = form_data.dict()
        # print(type(f1['form_Data']))

        # serializerobj = DisplayCarsSerializer(data=form_data,many=True)
        # print(form_data)
        # if(serializerobj.is_valid()):
        #     print("dfs")
        #     serializerobj.create(request)
        # else:
        #     print("e;lssds")

        return Response(status=status.HTTP_200_OK)


class DisplayCarCreate(APIView):
    def post(self, request):
        print(request.data)

        return Response(status=status.HTTP_200_OK)


class DisplayCarsStatusUpdator(generics.RetrieveUpdateAPIView):
    queryset = DisplayCars.objects.all()
    serializer_class = DisplayCarsSerializer
    lookup_field = 'id'


# class DisplayCarsPictureUpdator(generics.CreateAPIView):
#     parser_classes = [MultiPartParser]
#     queryset = DisplayCarImages.objects.all()
#     serializer_class = DisplayCarsImageCreateSerializer

    # def post(self,request):
    #     print(request.data)
    #
    #     return  Response(status= status.HTTP_201_CREATED)

class DisplayCarsPictureUpdator(APIView):

    parser_classes = [MultiPartParser]
    def post(self,request):
        print(request.data)
        print(request.FILES)
        displaycar = DisplayCars.objects.get(id= request.data['id'])
        for i in request.FILES:
            discar = DisplayCarImages.objects.create(car=displaycar, image=request.FILES[i])
            discar.save()
            print(i)
        print(request.data['id'])

        return Response(status=status.HTTP_201_CREATED)


class DisplayCarPatcher(generics.UpdateAPIView):
    serializer_class = DisplayCarsSerializer
    queryset = DisplayCars.objects.all()
    lookup_field = 'pk'




class FrontDeskDashboard(APIView):
    def get(self, request):
        pending_task = CarEnquiresmodel.objects.filter(status='pending').count()
        print(pending_task)
        online_advisors = AdvisorsOnline.objects.filter(online=True).count
        print(online_advisors)
        new_service_requests = Services.objects.filter(status='requested').count()
        print(new_service_requests)
        dash = Dashboard(pending_task,new_service_requests,online_advisors)

        serializer_obj = FrontDeskDashboardSerializer(dash)
        return Response(serializer_obj.data,status=status.HTTP_200_OK)
