from django.utils import timezone
from django.db import models
from django.db.models import TextField


class Student(models.Model):
    student_name = models.CharField(max_length=10)
    study_id = models.IntegerField(blank=True, null=True)

    student_qq = models.CharField(max_length=10, blank=True, null=True)
    student_email = models.EmailField(blank=True, null=True)
    student_tel = models.CharField(max_length=15,blank=True, null=True)

    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'

    YEAR_IN_SCHOOL_CHOICES = (
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior')

    )
    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
    )

    def __str__(self):
        return self.student_name


class Award(models.Model):
    award_name = models.CharField(max_length=30)
    student = models.ManyToManyField(Student, through='Awardship')
    get_time = models.DateTimeField()

    def __str__(self):
        return self.award_name


class Awardship(models.Model):
    awardship_name = models.CharField(max_length=20)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    Award = models.ForeignKey(Award, on_delete=models.CASCADE)
    Awardship_detail = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.awardship_name
