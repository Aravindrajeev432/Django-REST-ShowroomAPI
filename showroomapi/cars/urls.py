from django.urls import path
from .views import AddNewCar, CheckEngineNumber, GetDisplayCarsDetails, UserDisplayCars, GetFilterData

urlpatterns = [
    # get for retrive post for create
    path('stockcar', AddNewCar.as_view(), name="creating-cars"),
    path('check-enginenumber/<str:engine_number>', CheckEngineNumber.as_view(), name="check-enginenumber"),
    path('getdisplaycarsdetails', GetDisplayCarsDetails.as_view()),
    path('getdisplaycars', UserDisplayCars.as_view()),
    path('get-filter-data', GetFilterData.as_view()),


]
