# Generated by Django 3.0.6 on 2020-08-11 01:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_profile_ocupation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='ocupation',
        ),
    ]
