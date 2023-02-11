from rest_framework import serializers
from frontdesk.models import CarEnquiresmodel
from account.models import Account
from django.db.models import Q


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'username']

class EnquireySerilaizer(serializers.ModelSerializer):
    class Meta:
        model = CarEnquiresmodel
        fields = "__all__"



class CarEnquiresSerializer(serializers.ModelSerializer):
    def validate(self, data):
        if CarEnquiresmodel.objects.filter(Q(user_phone=data['user_phone']) & Q(status="pending")).count() > 1:
            car = CarEnquiresmodel.objects.filter(Q(user_phone=data['user_phone']) & Q(status="pending"))
            print(car)
            raise serializers.ValidationError("a request already made")
        return data

    class Meta:
        model = CarEnquiresmodel
        fields = "__all__"
        read_only_fields = ('status',)


class CarEnquiryListCreateSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField(read_only=True, format="%Y-%m-%d")
    def get_user(self, obj):
        try:
            is_auth_user = Account.objects.get(phone_number=obj.user_phone)

            return is_auth_user.username
        except Account.DoesNotExist:
            return None

    class Meta:
        model = CarEnquiresmodel
        fields = "__all__"

#
# class CarEnquireCreateSerializer(serializers.ModelSerializer):
#     print("en createserialix=zer")
#     user = serializers.SerializerMethodField()
#     status = serializers.SerializerMethodField()
#
#
#     # anonymous user is anonymous_user user is authenticated user
#     def get_user(self, obj):
#         user = self.context['request'].user
#         print(obj)
#         if user:
#             return None
#         else:
#             return user
#
#     def get_status(self, obj):
#         print(obj)
#         return self.context['status']
#
#     class Meta:
#         model = CarEnquires
#         fields = "__all__"
