# Generated by Django 4.0.4 on 2022-05-15 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0029_alter_graduation_observation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graduation',
            name='observation',
            field=models.TextField(default='obs', max_length=255),
        ),
    ]