from django.db import models

# Create your models here.

class user_cred(models.Model):
    username = models.CharField(max_length = 20, blank=False)
    password = models.CharField(max_length = 100, blank=False)
