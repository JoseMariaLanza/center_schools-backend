# Generated by Django 4.0.4 on 2022-05-17 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0040_alter_graduation_observation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
