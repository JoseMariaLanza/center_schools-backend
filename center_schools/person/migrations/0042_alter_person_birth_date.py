# Generated by Django 4.0.4 on 2022-05-17 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0041_alter_person_first_name_alter_person_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='birth_date',
            field=models.DateField(null=True),
        ),
    ]