from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from django.dispatch import receiver

USER_TYPE_CHOICES = (
    (1, 'livreur'),
    (2, 'fournisseur'),
    (3, 'modérateur'),
    (4, 'administrateur')
)

class User(AbstractUser):
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.username

@receiver(models.signals.post_save, sender=User)
def user_created(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 1:
            instance.groups.add(Group.objects.get(name='livreur'))
        elif instance.user_type == 2:
            instance.groups.add(Group.objects.get(name='fournisseur'))
        elif instance.user_type == 3:
            instance.groups.add(Group.objects.get(name='modérateur'))
        elif instance.user_type == 4:
            instance.groups.add(Group.objects.get(name='administrateur'))


class Fournisseur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='user')
    entreprise = models.TextField(max_length=200, verbose_name='entreprise')
    numTel = models.IntegerField(verbose_name='numéro de téléphone')
    adresse = models.TextField(max_length=500, verbose_name='adresse')

    def __str__(self):
        return self.entreprise