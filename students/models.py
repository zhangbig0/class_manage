from django.utils import timezone
from django.db import models
from django.db.models import TextField


class Student(models.Model):
    name = models.CharField(max_length=10)
    study_id = models.IntegerField(default=1)

    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'

    YEAR_IN_SCHOOL_CHOICES = (
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
    )
    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
    )

    def __str__(self):
        return self.name


class Award(models.Model):
    name = models.CharField(max_length=30)
    student = models.ManyToManyField(Student, through='Awardship')
    text = models.TextField(max_length=100)
    time = models.DateTimeField()

    def __str__(self):
        return self.name


class Awardship(models.Model):
    name = models.CharField(max_length=20)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    Award = models.ForeignKey(Award, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
