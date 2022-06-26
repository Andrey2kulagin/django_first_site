from django.db import models


# Create your models here.
class Task(models.Model):
    number = models.CharField("Phone number", max_length=15)
    name = models.CharField("Name", max_length=50)
    def __str__(self):
        return self.number
