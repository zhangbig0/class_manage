# Generated by Django 2.2.1 on 2019-11-23 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0010_auto_20191123_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False, verbose_name='学生学号'),
        ),
    ]