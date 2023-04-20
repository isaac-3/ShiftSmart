from django.db import models

# Create your models here.


class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30, unique=True)
    daysOff = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
