from django.db import models


class Course(models.Model):
    course_name = models.CharField(max_length=20, null=False, blank=False)
    course_credit = models.FloatField(verbose_name='绩点')

    def __str__(self):
        return '{}'.format(self.course_name)
