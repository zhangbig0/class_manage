# Generated by Django 2.2.1 on 2019-05-16 08:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20190516_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='awardship',
            name='date_get',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 16, 8, 59, 50, 65257, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='student',
            name='study_id',
            field=models.IntegerField(default=1),
        ),
    ]
