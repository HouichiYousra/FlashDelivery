# Generated by Django 3.0.3 on 2020-08-21 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commandes', '0006_auto_20200821_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livraison',
            name='code',
            field=models.TextField(max_length=200, verbose_name='code de validation'),
        ),
    ]
