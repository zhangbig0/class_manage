# Generated by Django 2.2.1 on 2019-11-23 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0012_auto_20191123_1348'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='awardship',
            options={'verbose_name': '获奖奖项', 'verbose_name_plural': '获奖奖项'},
        ),
        migrations.AlterField(
            model_name='student',
            name='year_in_school',
            field=models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior')], default='FR', max_length=2, verbose_name='学期'),
        ),
    ]