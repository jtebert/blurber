from django.contrib import admin
from models import Blurb, Genre

# Register your models here.

class GenreAdmin(admin.ModelAdmin):
    pass

admin.site.register(Genre, GenreAdmin)

class BlurbAdmin(admin.ModelAdmin):
    pass


admin.site.register(Blurb, BlurbAdmin)