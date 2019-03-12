from django.contrib import admin
from .models import Game, Publisher

# Register your models here.
admin.site.register(Publisher)
admin.site.register(Game)