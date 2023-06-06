from django.db import models

# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=17)
    description = models.TextField()
