from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import json

from rest_framework import generics
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

from django.db.models import Q
from account.models import Account
from .serializers import EmployeesSerializer
from account.custom_permissions import IsManager




class EmployeePagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 1000



class GetEmployees(generics.ListAPIView):
    permission_classes = [IsManager]
    model = Account
    serializer_class = EmployeesSerializer
    queryset = Account.objects.filter(~Q(is_admin=True)&~Q(role=None)).defer('password','address','is_admin','is_superadmin')
    pagination_class = EmployeePagination
