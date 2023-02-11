from django.db import models
from account.models import Account
from cars.models import DisplayCars
from django.core.validators import RegexValidator


# Create your models here.
class CarEnquiresmodel(models.Model):
    STATUS_CHOICES =[
        ('pending','pending'),
        ('completed','completed')
    ]

    phone_regex = RegexValidator(regex=r'^\d{10}$',
                                 message="Phone number should be 10 digits")
    user_phone = models.CharField(
        max_length=20, validators=[phone_regex], default='', blank=True
    )
    display_car = models.ForeignKey(DisplayCars, on_delete=models.SET)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100,null=True, choices=STATUS_CHOICES,default="pending")



