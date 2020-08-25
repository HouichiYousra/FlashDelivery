from django.core.mail import EmailMessage
from rest_framework import viewsets

from FlashDelivery import settings
from .policy import *
from .serializers import *


class emailView(viewsets.ModelViewSet):
    permission_classes = (EmailPolicy,)
    serializer_class = emailSerializer
    queryset = Email.objects.all()
    def perform_create(self, serializer):
        serializer.save()
        subject = serializer.data['subject']
        message = serializer.data['message']
        email_from = serializer.data['email_from']
        recipient = settings.EMAIL_HOST_USER
        email = EmailMessage(
            subject,
            message,
            email_from,
            recipient
        )
        email.send()