from django.db import models

class Reviews(models.Model):
    comment_text = models.CharField(max_length=500)
    creation_date = models.DatatimeField(auto_now=True, auto_now_add=True)
    game_reviewed = models.ForeignKey('Games', on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey('Users', on_delete=models.SET_NULL, null=True)

class Games(models.Model):
    category = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    publisher_name = models.ForeignKey('Publishers', on_delete=models.SET_NULL, null=True)
    year_released = models.DataField(max_length=30)

class Publishers(models.Model):
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)

