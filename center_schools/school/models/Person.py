from django.db import models
from user.models import User

from school.services.bussines.Enumerators import BloodType, SchoolRoles

from django.db.models.signals import post_save
from django.dispatch import receiver


class Person(models.Model):
    """User personal data

    Args:
        models (Person): User personal data to be used by an School
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
    first_name = models.CharField(
        max_length=100,
        null=True
    )
    last_name = models.CharField(
        max_length=100,
        null=True
    )
    birth_date = models.DateField(null=True)
    blood_type = models.CharField(
        max_length=2,
        choices=BloodType.choices,
        null=True,
        default=None
    )
    observation = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    status = models.CharField(
        max_length=11,
        choices=SchoolRoles.choices,
        default=SchoolRoles._GUEST,
    )

    def __str__(self):
        if self.last_name or self.first_name:
            return self.last_name + ', ' + self.first_name
        else:
            return self.user.email


@receiver(post_save, sender=User)
def create_person_assigned_to_user(sender, instance, created, **kwargs):
    if created:
        Person.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_person_assigned_to_user(sender, instance, created, **kwargs):
    instance.person.save()
