from django.db import models


class Review(models.Model):
    number_likes = models.IntegerField(default = 0)
    number_dislikes = models.IntegerField(default = 0)
    comment_text = models.CharField(max_length=500)
    creation_date = models.DateTimeField(auto_now=True)
    game_reviewed = models.ForeignKey('Game', on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey('accounts.CustomUser', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.comment_text

class Game(models.Model):
    category = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    publisher_name = models.ForeignKey('Publisher', on_delete=models.SET_NULL, null=True)
    year_released = models.DateField(max_length=30)
    game_content = models.TextField(null = True,default="")

    def __str__(self):
        return self.name

class Picture(models.Model):
    game_name = models.ForeignKey('Game', on_delete=models.SET_NULL, null=True)
    picture_path = models.CharField(max_length=100)

    def __str__(self):
        return self.game_name.name

class Video(models.Model):
    game_name = models.ForeignKey('Game', on_delete=models.SET_NULL, null=True)
    video_path = models.CharField(max_length=100)

    def __str__(self):
        return self.game_name.name


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class News(models.Model):
    news_title = models.CharField(max_length=100)
    news_content = models.TextField(null = True,default="")
    news_data = models.DateField(max_length=30)
    editor_name = models.CharField(max_length=100)

    def __str__(self):
        return self.news_title