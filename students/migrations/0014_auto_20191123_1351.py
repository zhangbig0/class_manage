# Generated by Django 2.2.1 on 2019-11-23 05:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0013_auto_20191123_1349'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='award',
            options={'ordering': ['get_time'], 'verbose_name': '比赛', 'verbose_name_plural': '比赛'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['student_id'], 'verbose_name': '学生', 'verbose_name_plural': '学生'},
        ),
    ]
