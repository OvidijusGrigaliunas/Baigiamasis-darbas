from django.db import models
from django.contrib.auth.models import User


class User_Data(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    height = models.FloatField()
    weight = models.FloatField()
    birthdate = models.DateField(default='2000-01-01')


class Category(models.Model):
    category_name = models.CharField(max_length=64)
    category_desc = models.TextField()
    unit_of_measurement = models.CharField(max_length=32)


class Record(models.Model):
    user = models.ForeignKey(User_Data, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    record_date = models.DateTimeField()
    record_value = models.FloatField()
