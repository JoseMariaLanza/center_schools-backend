# Generated by Django 4.0.4 on 2022-05-15 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0032_graduation_observation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='graduation',
            name='observation',
        ),
    ]
