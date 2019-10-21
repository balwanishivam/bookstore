from django.db import models
class book(models.Model):
    name=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    isbn=models.CharField(max_length=15)

# Create your models here.
