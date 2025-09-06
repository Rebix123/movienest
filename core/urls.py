from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('movie/<slug:slug>/', views.movie_detail, name='movie_detail'),
    path('movies/', views.movie_list, name='movie_list'),
    path('series/', views.series_list, name='series_list'),
    path('genres/', views.genre_list, name='genre_list'),
    path('categories/', views.category_list, name='category_list'),
    path('category/<int:category_id>/', views.movies_by_category, name='movies_by_category'),
    path('genre/<int:genre_id>/', views.movies_by_genre, name='movies_by_genre'),
    path('search/', views.search_movies, name='search_movies'),
    path('live/', views.live_matches, name='live'),
    path('livematch/<int:live_id>/', views.live_match_detail, name='live_details'),
]
