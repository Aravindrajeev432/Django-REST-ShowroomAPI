from django.db import models
from account.models import Account


# Create your models here.

class AdvisorsOnline(models.Model):
    advisor = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True)
    online = models.BooleanField(default=False)
