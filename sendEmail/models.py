from django.db import models


class Email (models.Model):
    subject = models.TextField(verbose_name='Titre')
    message = models.TextField(verbose_name='Message')
    email_from = models.EmailField(verbose_name='source')

    def __str__(self):
        return self.subject