from django.urls import path
from .views import CreateCustomer, GetCustomers, CarAvilabilty, GetFilterData, UpdateCustomer, AddDisplayCars,DisplayCarCreate,TestDisplayCars,DisplayCarsPictureUpdator,\
    DisplayCarsStatusUpdator,DisplayCarPatcher,FrontDeskDashboard

urlpatterns = [
    path('create-customer', CreateCustomer.as_view(), name='home'),
    path('get-customer', GetCustomers.as_view()),
    path('update-customer', UpdateCustomer.as_view()),
    path('check-car-availability', CarAvilabilty.as_view()),
    path('get-filter-data', GetFilterData.as_view()),
    path('add-display-cars', AddDisplayCars.as_view()),
    path('displaycarcreate',DisplayCarCreate.as_view()),
    path('test-displaycars', TestDisplayCars.as_view()),
    path('displaycarspictureupdator', DisplayCarsPictureUpdator.as_view()),
    path('displaycarsstatusupdator/<int:id>',DisplayCarsStatusUpdator.as_view()),
    path('displaycars/<int:pk>', DisplayCarPatcher.as_view()),
    path('dashboard-data',FrontDeskDashboard.as_view())

]
