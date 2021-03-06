from django.db import models
from django.template.defaultfilters import slugify

class Review(models.Model):
    number_likes = models.PositiveIntegerField(default = 0)
    number_dislikes = models.PositiveIntegerField(default = 0)
    comment_text = models.CharField(max_length=500)
    creation_date = models.DateTimeField(auto_now=True)
    game_reviewed = models.ForeignKey('Game', on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey('accounts.CustomUser', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.comment_text

    # def save(self, *args, **kwargs):
    #     if self.number_likes < 0:
    #         self.number_likes = 0
    #     if self.number_dislikes < 0:
    #         self.number_dislikes = 0
    #     super(Review, self).save(*args, **kwargs)

class Game(models.Model):
    category = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    publisher_name = models.ForeignKey('Publisher', on_delete=models.SET_NULL, null=True)
    year_released = models.DateField(max_length=30)
    game_content = models.TextField(null = True,default="")
    slug = models.SlugField()
    image = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name) 
        super(Game, self).save(*args, **kwargs)

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
    video_infor_pic_path = models.CharField(max_length=100)

    def __str__(self):
        return self.game_name.name


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)

    def __str__(self):
        return self.name