from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from course.models import Class


# Create your models here.

class Position(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    created_date = models.DateField(default=timezone.now())


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student')
    student_id = models.CharField(max_length=32)
    level = models.CharField(max_length=16, blank=True, null=True)
    enroll_courses = models.ManyToManyField(Class)
    father_name = models.CharField(max_length=128, null=True, blank=True)
    mother_name = models.CharField(max_length=128, null=True, blank=True)
    phone_number = models.CharField(max_length=16, blank=True)

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def email(self):
        return self._email

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name + " " + self.student_id


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    teacher_id = models.CharField(max_length=32)
    position = models.ManyToManyField(Position)
    date_joined = models.DateField(blank=True)
    is_principle = models.BooleanField(default=False)

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def email(self):
        return self._email

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name + " " + self.teacher_id


class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    children = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Administrator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.ManyToManyField(Position)

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def email(self):
        return self._email

    def __str__(self):
        return self.user.username
