from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    
    def __str__(self):
        return f"{self.username}"

class Listing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listings")
    Title = models.CharField(max_length=64)
    Description = models.TextField()
    Image = models.URLField(blank=True)
    Category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name="listings")
    Date = models.DateField()
    Time = models.TimeField()
    Active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.Title}"

class Category(models.Model):
    category = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.category}"

class Order(models.Model):
    By = models.CharField(max_length=30)
    action = models.CharField(max_length=30, null=True) 

    def __str__(self):
        return f"{self.By}"