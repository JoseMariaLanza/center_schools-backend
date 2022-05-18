# Generated by Django 4.0.4 on 2022-05-15 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0035_graduation_observation_graduation_qualification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graduation',
            name='observation',
            field=models.TextField(default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='graduation',
            name='qualification',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=2, null=True),
        ),
    ]