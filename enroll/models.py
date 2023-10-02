from django.db import models
from datetime import date
# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=70)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)
    current_date = models.DateTimeField(auto_now_add=True)