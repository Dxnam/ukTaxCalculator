from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    name = models.CharField(max_length=255)
    allowance = models.IntegerField(null=True)
    salary = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.name}"