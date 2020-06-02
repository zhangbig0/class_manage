from django.utils import timezone
from django.db import models
from django.db.models import TextField, SET_NULL
from django.contrib.auth.models import User
from django.urls import reverse

from course.models import Course


class Student(models.Model):
    student_name = models.CharField(max_length=10, verbose_name='学生姓名', null=False, error_messages={
        'required': '姓名不能为空'
    })
    student_id = models.IntegerField(primary_key=True, blank=False, null=False, verbose_name='学生学号', default=0)
    student_qq = models.CharField(max_length=10, blank=True, null=True, verbose_name='学生qq')
    student_email = models.EmailField(blank=True, null=True, verbose_name='学生邮箱')
    student_tel = models.CharField(max_length=15, blank=True, null=True, verbose_name='学生电话')
    user = models.OneToOneField(User, on_delete=models.SET_NULL, related_name="student", null=True)

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
        verbose_name='学期'
    )

    def get_absolute_url(self):
        return reverse('student:award-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.student_name

    class Meta:
        ordering = ['student_id']
        verbose_name = '学生'
        verbose_name_plural = '学生'


class Award(models.Model):
    award_name = models.CharField(max_length=30, verbose_name='赛事')
    student = models.ManyToManyField(Student, through='Awardship', verbose_name='参与学生')
    get_time = models.DateTimeField(verbose_name='比赛时间')

    def __str__(self):
        return self.award_name

    class Meta:
        ordering = ['get_time']
        verbose_name = '比赛'
        verbose_name_plural = '比赛'


class Awardship(models.Model):
    awardship_name = models.CharField(max_length=20, verbose_name='获奖详情')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='awardship_student',
                                verbose_name='获奖学生')
    award = models.ForeignKey(Award, on_delete=models.CASCADE, related_name='awardship_award', verbose_name='比赛')
    awardship_detail = models.TextField(blank=True, null=True, verbose_name='获奖详情')

    def __str__(self):
        return self.awardship_name

    class Meta:
        verbose_name = '获奖奖项'
        verbose_name_plural = '获奖奖项'


class Grade(models.Model):
    student = models.ForeignKey(Student, related_name='student', verbose_name='学生', on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey(Course, related_name='course', verbose_name='课程', on_delete=models.SET_NULL, null=True)
    grade = models.FloatField(null=False, verbose_name='成绩')
    GPA = models.FloatField(verbose_name='绩点')

    SEMESTER_SCHOOL_CHOICE = (
        (1, '学期一'), (2, '学期二'), (3, '学期三'), (4, '学期四'), (5, '学期五'), (6, '学期六'), (7, '学期七'), (8, '学期八')
    )

    semester = models.IntegerField(
        choices=SEMESTER_SCHOOL_CHOICE,
        verbose_name='学期',
        default=1
    )

    def __str__(self):
        return 'grade {} {}'.format(self.student.student_name, self.course.course_name)
