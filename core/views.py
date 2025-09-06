from django.shortcuts import render, get_object_or_404
from . import models

def home(request):
    categories = models.Category.objects.all()
    movies = models.Movie.objects.all().distinct().order_by('-updated_at')[:7]
    popular_movies = models.Movie.objects.filter(rating__gte=4).order_by('-rating')[:7]
    series = models.Movie.objects.filter(episodes__isnull=False).distinct().order_by('-updated_at')[:7]
    live= models.Live.objects.all().order_by('-id')[:3]

    context = {
        'categories': categories,
        'movies': movies,
        'popular_movies': popular_movies,
        'series': series,
        'live': live,
    }
    return render(request, 'index.html', context)

def movie_detail(request, slug):
    movie = get_object_or_404(models.Movie, slug=slug)
    related_movies = models.Movie.objects.filter(category=movie.category).exclude(id=movie.id)[:4]

    episodes = movie.episodes.all()

    context = {
        "movie": movie,
        "related_movies": related_movies,
        "episodes": episodes
    }
    return render(request, "movie_detail.html", context)

def movie_list(request):
    movies = models.Movie.objects.all().order_by('title')
    context = {
        "movies": movies
    }
    return render(request, "movie_list.html", context)

def series_list(request):
    series = models.Movie.objects.filter(episodes__isnull=False).distinct()
    context = {
        "series": series
    }
    return render(request, "series.html", context)

def genre_list(request):
    genres = models.Genre.objects.all()
    context = {
        "genres": genres
    }
    return render(request, "genre.html", context)

def category_list(request):
    categories = models.Category.objects.all()
    context = {
        "categories": categories
    }
    return render(request, "category.html", context)


def movies_by_category(request, category_id):
    category = get_object_or_404(models.Category, id=category_id)
    movies = models.Movie.objects.filter(category=category)

    context = {
        'category': category,
        'movies': movies
    }
    return render(request, 'catlist.html', context)

def movies_by_genre(request, genre_id):
    genre = get_object_or_404(models.Genre, id=genre_id)
    movies = models.Movie.objects.filter(genres=genre)

    context = {
        'genre': genre,
        'movies': movies
    }
    return render(request, 'genrelist.html', context)

def search_movies(request):
    query = request.GET.get('q')  
    results = []

    if query:
        results = models.Movie.objects.filter(title__icontains=query)  

    context = {
        'results': results,
        'query': query,
    }
    return render(request, 'search.html', context)

def live_matches(request):
    lives = models.Live.objects.all()
    context = {
        'lives': lives
    }
    return render(request, 'live_matches.html', context)

def live_match_detail(request, live_id):
    live = get_object_or_404(models.Live, id=live_id)
    context = {
        'live': live
    }
    return render(request, 'live_match_detail.html', context)
