# Generated by Django 3.0.6 on 2020-08-11 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0006_merge_20200810_2332'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='ocupation',
            field=models.TextField(blank=True, null=True),
        ),
    ]
