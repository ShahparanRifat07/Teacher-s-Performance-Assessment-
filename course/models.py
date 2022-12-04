from django.db import models
from django.utils import timezone


# from stakeholder.models import Teacher


# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=255)
    course_code = models.CharField(max_length=128)
    course_description = models.TextField(null=True, blank=True)
    created_date = models.DateField(default=timezone.now())

    def __str__(self):
        return self.title


class Class(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    class_teacher = models.ForeignKey('stakeholder.Teacher', on_delete=models.CASCADE)
    section = models.CharField(max_length=8)
    created_date = models.DateField(default=timezone.now())

    def __str__(self):
        return self.course.title + "_" + self.section
