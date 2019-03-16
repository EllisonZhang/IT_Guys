from django.contrib import admin
from .models import Game, Publisher, Review, Picture

# Register your models here.
admin.site.register(Publisher)
admin.site.register(Game)
admin.site.register(Review)
admin.site.register(Picture)
