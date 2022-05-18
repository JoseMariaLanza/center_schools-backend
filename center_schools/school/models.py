from django.db import models
from core import models as CoreAppModels
from django.db.models.signals import post_save
from django.dispatch import receiver


class Person(models.Model):
    """User personal data

    Args:
        models (Person): User personal data to be used by an School
    """

    class BloodType(models.TextChoices):
        """Blood types choices  A, B, AB and O"""
        A_TYPE = 'A'
        B_TYPE = 'B'
        AB_TYPE = 'AB'
        O_TYPE = '0'

    class Status(models.TextChoices):
        """Statusses for a person member of a School"""
        INSTRUCTOR = 'Instructor',
        STUDENT = 'Student',
        UNSUSCRIBED = 'Unsuscribed',
        EXPULSED = 'Expulsed',
        GUEST = 'Guest'

    user = models.OneToOneField(
        CoreAppModels.User,
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
        choices=Status.choices,
        default=Status.GUEST,
    )

    def __str__(self):
        if self.last_name or self.first_name:
            return self.last_name + ', ' + self.first_name
        else:
            return self.user.email


@receiver(post_save, sender=CoreAppModels.User)
def create_person_assigned_to_user(sender, instance, created, **kwargs):
    if created:
        Person.objects.create(user=instance)


@receiver(post_save, sender=CoreAppModels.User)
def save_person_assigned_to_user(sender, instance, created, **kwargs):
    instance.person.save()


class Graduation(models.Model):
    """A person have many graduations

    Args:
        models (Graduation): A person who belongs to a school(group)
        can have multiple graduations for different schools over the years
    """

    class Graduations(models.TextChoices):
        """Graduation list"""
        _10th_GUP = '10 GUP'
        _9th_GUP = '9 GUP'
        _8th_GUP = '8 GUP'
        _7th_GUP = '7 GUP'
        _6th_GUP = '6 GUP'
        _5th_GUP = '5 GUP'
        _4th_GUP = '4 GUP'
        _3rd_GUP = '3 GUP'
        _2nd_GUP = '2 GUP'
        _1st_GUP = '1 GUP'
        _I_DAN = 'I DAN'
        _II_DAN = 'II DAN'
        _III_DAN = 'III DAN'
        _IV_DAN = 'IV DAN'
        _V_DAN = 'V DAN'
        _VI_DAN = 'VI DAN'
        _VII_DAN = 'VII DAN'
        _VIII_DAN = 'VIII DAN'
        _IX_DAN = 'IX DAN'

    class Statusses(models.TextChoices):
        PASSED = 'Approved'
        FAILED = 'Not Approved'

    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
    )
    current_graduation = models.CharField(
        max_length=10,
        choices=Graduations.choices,
        null=True
    )
    apply_for = models.CharField(
        max_length=10,
        choices=Graduations.choices,
        null=True
    )
    weight = models.DecimalField(
        max_digits=5,
        decimal_places=3,
        null=True,
        default=None
    )
    graduation_date = models.DateTimeField(
        auto_now=False,
        auto_now_add=False
    )
    evaluators = models.ManyToManyField(
        Person,
        related_name='evaluators'
    )
    graduation_place = models.CharField(max_length=255)
    status = models.CharField(
        max_length=20,
        choices=Statusses.choices,
        default=None,
    )
    qualification = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        null=True,
        default=None
    )
    observation = models.TextField(
        max_length=255,
        null=True,
        blank=True
    )
    certification_id = models.CharField(max_length=30, default=None)

    def get_graduation(self):
        if self.status == self.Statusses.PASSED:
            return self.apply_for
        else:
            return self.graduation_at_date

    def __str__(self):
        return str(self.person) + ' ' + str(self.get_graduation())
