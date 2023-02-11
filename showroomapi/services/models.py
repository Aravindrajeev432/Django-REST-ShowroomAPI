from django.db import models
from account.models import Account
from cars.models import Cars,CarParts
from pyasn1.compat.octets import null


# Create your models here.
class Services(models.Model):
    SERVICE_STATUS_CHOICES = [
        ('requested', 'requested'),
        ('assigned', 'assigned'),
        ('in-bay', 'in-bay'),
        ('billing', 'billing'),
        ('finished', 'finished'),

    ]
    user = models.ForeignKey(
        Account, on_delete=models.SET_NULL, null=True, related_name='user', blank=True
    )
    car = models.ForeignKey(
        Cars, on_delete=models.SET_NULL, null=True, related_name='user_car', blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=SERVICE_STATUS_CHOICES)
    finished_at = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    advisor = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True)
    parts_used = models.ManyToManyField(CarParts)
    is_free = models.BooleanField(default=False)


class ServiceInfo(models.Model):
    universal_car_number = models.CharField(max_length=100, unique=True)
    first_service_km = models.IntegerField()
    first_service_month = models.IntegerField()
    second_service_km = models.IntegerField()
    second_service_month = models.IntegerField()
    third_service_km = models.IntegerField()
    third_service_month = models.IntegerField()
    number_of_free_services = models.IntegerField()
    afterwards_service_km = models.IntegerField()
    afterwards_service_month = models.IntegerField()
    base_fee = models.IntegerField()


class ServiceHistory(models.Model):
    service = models.ForeignKey(Services,on_delete=models.SET_NULL,null=True,related_name='service_log')
    amount = models.IntegerField()
    parts_total = models.IntegerField()
    labour_charge = models.IntegerField()

    is_free = models.BooleanField()


class BayDetails(models.Model):
    BAY_STATUS_CHOICES = [
        ('busy', 'busy'),
        ('free', 'free'),
    ]
    created_at = models.DateTimeField(auto_now_add=True)
    bay_number = models.IntegerField(unique=True)
    status = models.CharField(max_length=100, choices=BAY_STATUS_CHOICES)
    mechanic_1 = models.ForeignKey(Account, on_delete=models.SET_NULL, related_name='bay_mechanic_1', null=True, blank=True)


class BayCurrentJob(models.Model):
    bay = models.ForeignKey(
        BayDetails,
        on_delete=models.SET_NULL,
        related_name='related_bay',
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    current_job = models.ForeignKey(Services, on_delete=models.SET_NULL, related_name='service_bay', null=True,
                                    blank=True)
    mechanic_1 = models.ForeignKey(Account, on_delete=models.SET_NULL, related_name='mechanic_1', null=True, blank=True)
    mechanic_2 = models.ForeignKey(Account, on_delete=models.SET_NULL, related_name='mechanic_2', null=True, blank=True)


