# Generated by Django 2.1.8 on 2020-06-02 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0017_auto_20200528_2248'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=20)),
                ('course_credit', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.FloatField(verbose_name='成绩')),
                ('GPA', models.FloatField(verbose_name='绩点')),
                ('semester', models.IntegerField(choices=[(1, '学期一'), (2, '学期二'), (3, '学期三'), (4, '学期四'), (5, '学期五'), (6, '学期六'), (7, '学期七'), (8, '学期八')], default=1, verbose_name='学期')),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='course', to='students.Course', verbose_name='课程')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student', to='students.Student', verbose_name='学生')),
            ],
        ),
    ]