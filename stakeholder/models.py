from django.db import models
from django.contrib.auth import User
from django.utils import timezone
# Create your models here.

class Student(models.Model):
    user = models.OneToOneField(User, )

class Teacher(models.Model):
    pass

class Parent(models.Model):
    pass

class Adminstrator(models.Model):
    pass
