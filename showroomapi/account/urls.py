from django.urls import path
from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import (

    TokenRefreshView,
)

from .views import StaffLogin, AddManager, AddEmployee

urlpatterns = [
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('staff-login', StaffLogin.as_view(), name="staff login"),
    path('create-manager', AddManager.as_view(), name="add manager"),
    path('create-employee', AddEmployee.as_view(), name="add_employee")
]
