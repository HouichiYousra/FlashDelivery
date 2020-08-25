# Generated by Django 3.0.3 on 2020-08-21 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commandes', '0005_auto_20200821_1615'),
    ]

    operations = [
        migrations.RenameField(
            model_name='livraison',
            old_name='Commande',
            new_name='commande',
        ),
        migrations.AlterField(
            model_name='commande',
            name='etat',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Nouvelle'), (2, 'validée'), (3, 'suppriméée')]),
        ),
    ]