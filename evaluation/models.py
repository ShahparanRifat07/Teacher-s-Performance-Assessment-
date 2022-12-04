from django.db import models
from django.utils import timezone


class Factor(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)
    created_date = models.DateField(default=timezone.now())
