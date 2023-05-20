from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Computer)
admin.site.register(GamesType)
admin.site.register(Game)
admin.site.register(Player)
admin.site.register(Result)
