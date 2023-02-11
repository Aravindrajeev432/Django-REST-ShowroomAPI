from rest_framework import serializers
from .models import AdvisorsOnline
from services.models import BayDetails, BayCurrentJob, Services
from account.models import Account
from cars.models import Cars


class CarDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = ['model_name', 'model_year']


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['username', 'id']


class MakeOnlineSerializer(serializers.ModelSerializer):
    advisor = AccountSerializer()

    class Meta:
        model = AdvisorsOnline
        fields = '__all__'


class BayCurrentJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = BayCurrentJob
        fields = '__all__'


class SerivesCurrentSerializer(serializers.ModelSerializer):
    service_bay = BayCurrentJobSerializer(many=True, read_only=True)
    car = CarDetailsSerializer()
    user = AccountSerializer()

    class Meta:
        model = Services
        fields = '__all__'


class JobAssignBaySerializer(serializers.ModelSerializer):
    # bay = BayCurrentJobSerializer(many=True)
    class Meta:
        model = BayCurrentJob
        fields = '__all__'


class AdvisorDashboardSerializer(serializers.Serializer):
    service_done = serializers.CharField(max_length=100)
    ongoing_jobs = serializers.CharField(max_length=100)
    free_bays = serializers.CharField(max_length=100)
