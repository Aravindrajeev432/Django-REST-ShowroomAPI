from rest_framework import serializers

from account.models import Account


class EmployeesSerializer(serializers.ModelSerializer):
    """Employee serializer"""

    class Meta:
        model = Account
        fields = ['id', 'username', 'email', 'phone_number', 'last_login', 'role']
