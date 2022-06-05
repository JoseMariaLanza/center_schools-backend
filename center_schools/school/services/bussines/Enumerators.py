from django.db import models


class BloodType(models.TextChoices):
    """Blood types choices  A, B, AB and O"""
    _A_TYPE = 'A'
    _B_TYPE = 'B'
    _AB_TYPE = 'AB'
    _O_TYPE = '0'


class SchoolRoles(models.TextChoices):
    """Roles for a person member of a School"""
    _INSTRUCTOR = 'Instructor',
    _STUDENT = 'Student',
    _UNSUSCRIBED = 'Unsuscribed',
    _EXPULSED = 'Expulsed',
    _GUEST = 'Guest'


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


class EvaluationStatusses(models.TextChoices):
    _PASSED = 'Approved'
    _FAILED = 'Not approved'
