# Generated by Django 2.2.1 on 2019-05-17 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_auto_20190517_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_email',
            field=models.EmailField(default='xxx@xx.com', max_length=254),
        ),
        migrations.AddField(
            model_name='student',
            name='student_qq',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='student_tel',
            field=models.CharField(default=0, max_length=15),
            preserve_default=False,
        ),
    ]
