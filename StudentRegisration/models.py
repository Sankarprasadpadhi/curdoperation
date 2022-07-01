from django.db import models

class StudentData(models.Model):
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    mobile = models.CharField(max_length=10, unique=True)
    address = models.CharField(max_length=500, null=True,blank=True)
    email = models.CharField(max_length=200, unique=True)
