# Generated by Django 2.0.2 on 2020-08-08 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_profile_ocupation'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='category_id',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='ocupation',
            field=models.TextField(null=True),
        ),
    ]
