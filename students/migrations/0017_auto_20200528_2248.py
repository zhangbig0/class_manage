# Generated by Django 2.1.8 on 2020-05-28 14:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0016_auto_20200528_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_name',
            field=models.CharField(error_messages={'required': '姓名不能为空'}, max_length=10, verbose_name='学生姓名'),
        ),
        migrations.AlterField(
            model_name='student',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student', to=settings.AUTH_USER_MODEL),
        ),
    ]