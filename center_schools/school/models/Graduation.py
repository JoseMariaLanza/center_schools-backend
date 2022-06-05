from django.db import models
from .Person import Person

from school.services.bussines.Enumerators import Graduations, \
    EvaluationStatusses


class Graduation(models.Model):
    """A person have many graduations

    Args:
        models (Graduation): A person who belongs to a school(group)
        can have multiple graduations for different schools over the years
    """

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
        choices=EvaluationStatusses.choices,
        default=EvaluationStatusses._FAILED,
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
        if self.status == EvaluationStatusses._PASSED:
            return self.apply_for
        else:
            return self.graduation_at_date

    def __str__(self):
        return str(self.person) + ' ' + str(self.get_graduation())
