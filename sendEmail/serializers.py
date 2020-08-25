from rest_framework import serializers

from sendEmail.models import *


class emailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = '__all__'