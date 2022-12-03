# Generated by Django 4.1.3 on 2022-12-02 22:52

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stakeholder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('course_code', models.CharField(max_length=128)),
                ('created_date', models.TextField(default=datetime.datetime(2022, 12, 2, 22, 52, 45, 612817, tzinfo=datetime.timezone.utc))),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(max_length=8)),
                ('created_date', models.TextField(default=datetime.datetime(2022, 12, 2, 22, 52, 45, 613862, tzinfo=datetime.timezone.utc))),
                ('class_teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stakeholder.teacher')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course')),
            ],
        ),
    ]
