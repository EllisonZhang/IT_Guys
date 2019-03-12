from django.contrib import admin
from .models import Game, Publisher, Review

# Register your models here.
admin.site.register(Publisher)
admin.site.register(Game)
admin.site.register(Review)