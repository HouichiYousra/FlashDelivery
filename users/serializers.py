from allauth.account.utils import setup_user_email
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers

from users.adapters import CustomAccountAdapter
from users.models import *


class CustomRegisterSerializer(RegisterSerializer):
    user_type = serializers.ChoiceField(choices=USER_TYPE_CHOICES)

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['user_type'] = self.validated_data.get('user_type', '')
        return data_dict

class UserSerializer(serializers.ModelSerializer):
    class meta:
        model = User
        fields = '__all__'


class FournisseurSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    class meta:
        model = User
        fields = '__all__'