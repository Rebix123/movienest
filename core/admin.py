from django.contrib import admin
from .models import Movie, Episode, Genre, Category, Live, Team

class EpisodeInline(admin.TabularInline):
    model = Episode
    extra = 1  


class MovieAdmin(admin.ModelAdmin):
    inlines = [EpisodeInline]


admin.site.register(Genre)
admin.site.register(Category)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Team)
admin.site.register(Live)
