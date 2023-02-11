from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import json
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Account
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .custom_permissions import IsManager


# Create your views here.


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['role'] = user.role
        token['is_customer'] = user.is_customer
        token['phone_number'] = user.phone_number
        token['is_pda'] = user.is_pda
        token['is_staff'] = user.is_staff
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class StaffLogin(APIView):
    def post(self, request):
        print(request)
        body = request.body.decode("utf-8")
        print(body)
        body = json.loads(body)
        # print(body['username'])

        # try:
        #     user = Account.objects.get(phone_number=body["phone_number"])
        #     print(user)
        #     if user
        # except Account.DoesNotExist:
        #
        # print(user)
        # if user is not None:
        #     print("success")
        return Response({'message': "success"}, status=status.HTTP_200_OK)

    def get(self, request):
        return Response({}, status=status.HTTP_200_OK)

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }


class AddManager(APIView):
    def get(self, request):
        post = {
            "phone_number": "",
            "username": "",
            "password": "",
            "email": ""

        }

        return Response(post, status=status.HTTP_200_OK)

    def post(self, request):
        body = request.body.decode("utf-8")
        print(body)
        body = json.loads(body)

        user = Account.objects.create_manager(email=body['email'], username=body['username'],
                                              phone_number=body['phone_number'], password=body['username'])
        print(user)
        return Response(status=status.HTTP_201_CREATED)


class MycustomMixin(object):
    def get(self, request):
        print("hello")
        return Response(status=status.HTTP_404_NOT_FOUND)


class AddEmployee(MycustomMixin, APIView):
    permission_classes = [IsManager]

    def post(self, request):
        user = request.user
        print(user)
        body = request.body.decode("utf-8")
        print(body)
        body = json.loads(body)
        if Account.objects.filter(Q(phone_number=body['phone_number']) & Q(is_staff=True)).exists():
            return Response(status=status.HTTP_409_CONFLICT)
        email = body['email']
        username = body['username']
        phone_number = body['phone_number']
        password = body['username'] + "123"
        if body['role'] == "Advisor":
            # Account.objects.create_advisor(email=email, username=username, phone_number=phone_number, password=password)
            return Response(status=status.HTTP_201_CREATED)
        elif body['role'] == "Front_desk":
            Account.objects.create_front_desk(email=email, username=username,
                                              phone_number=phone_number, password=password)
            return Response(status=status.HTTP_201_CREATED)
        elif body['role'] == 'Mechanic':
            Account.objects.create_mechanic(email=email,username=username,phone_number=phone_number,password=password)
            return Response(status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_502_BAD_GATEWAY, statusText="email already taken")

    def get(self, request):
        user = request.user
        print(user)
        # body = request.body.decode("utf-8")
        print(request.body)

        print("get")
        return Response(status=status.HTTP_200_OK)
