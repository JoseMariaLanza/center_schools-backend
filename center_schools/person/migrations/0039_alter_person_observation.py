# Generated by Django 4.0.4 on 2022-05-17 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0038_alter_person_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='observation',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]