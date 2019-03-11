from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    comment_text = models.CharField(max_length=500)
    creation_date = models.DateTimeField(auto_now=True)
    game_reviewed = models.ForeignKey('Game', on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey('UserProfile', on_delete=models.SET_NULL, null=True)

class Game(models.Model):
    category = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    publisher_name = models.ForeignKey('Publisher', on_delete=models.SET_NULL, null=True)
    year_released = models.DateField(max_length=30)
    
    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)    

    # The additional attributes we wish to include.
    dateOfBirth=models.DateField(auto_now=False)

    # Override the __unicode__() method to return out something meaningful!
    def __str__(self):
        return self.user