from django.db import models

class user(models.Model):
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=30)