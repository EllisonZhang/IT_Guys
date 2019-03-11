from django.contrib import admin
from .models import Game, UserProfile, Publisher

# Register your models here.
admin.site.register(Publisher)
admin.site.register(UserProfile)
admin.site.register(Game)