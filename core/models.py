from django.db import models
from django.contrib.auth.models import User


class Info(models.Model):
    username = models.CharField(max_length=60, null=False, blank=False)
    password = models.CharField(max_length=60, null=False, blank=False)
    
    def __str__(self):
        return self.username

class AdminLogin(models.Model):
    username = models.CharField(max_length=60, null=False, blank=False)
    password = models.CharField(max_length=60, null=False, blank=False)