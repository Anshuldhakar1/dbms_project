from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    
    def __str__(self):
        return f"{self.username}"

class Listing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listings")
    Title = models.CharField(max_length=64)
    Description = models.TextField()
    Bid = models.OneToOneField('Bid', blank=True, null=True, on_delete=models.CASCADE, related_name="listing")
    Image = models.ImageField(blank=True)
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

class Bid(models.Model):
    bidder = models.ForeignKey(User, null=True, default=None, on_delete=models.CASCADE, related_name="BID")
    bid = models.FloatField()
    # Bid has one to one relationship with Listing

    def __str__(self):
        return f"{self.listing} for ${self.bid}"

class Order(models.Model):
    By = models.CharField(max_length=30)
    action = models.CharField(max_length=30, null=True) 

    def __str__(self):
        return f"{self.By}"

class Comment(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comments")
    commentor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    comment = models.TextField()

    def __str__(self):
        return f"{self.listing}"

class Watchlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="watchlist")
    listings = models.ManyToManyField(Listing, blank=True, related_name="watchlist")

    def __str__(self):
        return f"{self.user}"