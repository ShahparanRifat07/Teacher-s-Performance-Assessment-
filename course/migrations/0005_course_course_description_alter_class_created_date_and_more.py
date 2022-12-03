# Generated by Django 4.1.3 on 2022-12-03 03:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_alter_class_created_date_alter_course_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='class',
            name='created_date',
            field=models.TextField(default=datetime.datetime(2022, 12, 3, 3, 9, 32, 521348, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='course',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2022, 12, 3, 3, 9, 32, 521348, tzinfo=datetime.timezone.utc)),
        ),
    ]