# Generated by Django 4.0.4 on 2022-05-15 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0036_alter_graduation_observation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graduation',
            name='qualification',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=4, null=True),
        ),
    ]