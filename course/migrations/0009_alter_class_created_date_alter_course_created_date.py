# Generated by Django 4.1.3 on 2022-12-19 21:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_alter_class_created_date_alter_course_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2022, 12, 19, 21, 44, 46, 363892, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='course',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2022, 12, 19, 21, 44, 46, 362892, tzinfo=datetime.timezone.utc)),
        ),
    ]
