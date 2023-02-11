from django.urls import path
from .views import GetEmployees

urlpatterns=[
    path('get-employees',GetEmployees.as_view())
]