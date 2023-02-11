from rest_framework import serializers
from cars.models import Cars, DisplayCars, DisplayCarImages
from services.models import Services, ServiceInfo,ServiceHistory
from django.db.models import Q
import datetime
from dateutil import relativedelta


class DisplaySingleCarImageSerializer(serializers.HyperlinkedModelSerializer):
    # pk = self.context['pk']
    # image = serializers.HyperlinkedRelatedField(view_name='image',read_only=True)
    asd = serializers.SerializerMethodField()

    def get_asd(self, request):
        print(self.context['id'])

        return None

    class Meta:
        model = DisplayCarImages
        fields = ('image', 'asd')


class MyCarsSerializer(serializers.ModelSerializer):
    # def __init__(self,context):
    #     print("in init")
    #     print(self.request)

    last_service_date = serializers.SerializerMethodField()
    is_service_needed = serializers.SerializerMethodField()
    current_service_status = serializers.SerializerMethodField()

    def get_current_service_status(self, instance):
        cur_service_status = Services.objects.filter(Q(car=instance) & ~Q(status='finished'))[:1]
        # print(f"cur_service_status_count{cur_service_status.count()}")
        if cur_service_status.count() == 1:
            # print("ome")
            for i in cur_service_status:
                # print(i.status)
                c_s_s = i.status
            return c_s_s
        else:
            return None

    # image = serializers.SerializerMethodField()
    #
    # def get_image(self, instance):
    #
    #     print(instance.model_name)
    #     print(instance.model_year)
    #     print("--")
    #     try:
    #         car = DisplayCars.objects.get(model_name=instance.model_name, model_year=instance.model_year)
    #         print(car.id)
    #         print(DisplayCarImages.objects.filter(car=car))
    #         print("---")
    #         # data = DisplaySingleCarImageSerializer(DisplayCarImages.objects.filter(car=car)
    #         #                                        ).data
    #         # data = DisplaySingleCarImageSerializer(car.id).data
    #
    #         return DisplaySingleCarImageSerializer(DisplayCarImages.objects.filter(car=car)
    #                                                ,many=True,  read_only=True,context={'id':car.id}).data
    #     except DisplayCars.DoesNotExist:
    #         pass
    #     return None

    def get_last_service_date(self, instance):
        last_service_date = Services.objects.filter(car=instance).order_by('-finished_at')[:1]
        if last_service_date.exists():
            print("%%%")
            for i in last_service_date:
                l_s_d = i.finished_at

            return l_s_d
        else:
            return None

        return None

    def get_is_service_needed(self, instance):
        print(instance.model_name)

        try:
            service_info = ServiceInfo.objects.get(universal_car_number=instance.universal_car_number)
        except ServiceInfo.DoesNotExist:

            return None

        number_of_services = Services.objects.filter(car=instance.id).count()
        # print(f"number of service-{number_of_services}")
        delivered_date = Cars.objects.get(id=instance.id)
        r = relativedelta.relativedelta(datetime.date.today(), delivered_date.delivered_date)
        print(f'number of services {number_of_services}')
        if number_of_services == 0:

            # print(f"{datetime.date.today()}")
            # print(f"d_date-{delivered_date.delivered_date}")
            # print(f"first month-{service_info.first_service_month}")
            print(f'r months {r.months}')
            if r.months >= service_info.first_service_month:
                return "first"

        elif number_of_services == 1:
            if r.months >= service_info.second_service_month:
                return "seocond"

        elif number_of_services == 2:
            if r.months >= service_info.third_service_month:
                return "third"

        elif number_of_services == 3:

            last_service_date = Services.objects.filter(car=instance).order_by('-finished_at')[:1]
            r = relativedelta.relativedelta(datetime.date.today(), last_service_date.finished_at)
            if r.months >= service_info.afterwards_service_month:
                return "afterwards"

        return None

    class Meta:
        model = Cars
        fields = '__all__'
class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = ['model_name','model_year',]

class ServiceSerializer(serializers.ModelSerializer):
    car=CarSerializer()
    class Meta:
        model= Services
        fields = ['id','created_at','status','is_free','car','advisor']

class ServiceHistorySerializer(serializers.ModelSerializer):
    service = ServiceSerializer()
    class Meta:
        model = ServiceHistory
        fields= '__all__'
