# Generated by Django 2.2.1 on 2019-05-16 09:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_auto_20190516_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='awardship',
            name='date_get',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
