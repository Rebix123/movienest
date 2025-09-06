from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(max_length=30, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'
    

    def __str__(self):
        return self.title
    
    
        
class Genre(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Movie(models.Model):
    title = models.CharField(max_length=200, unique = True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
    genres = models.ManyToManyField('Genre')
    description = models.TextField()
    image = models.ImageField(upload_to='movies/')
    link = models.CharField(max_length=300)
    streaming = models.CharField(max_length=300, blank=True, null=True)
    size = models.CharField(max_length=300, blank=True, null=True)
    trailer = models.URLField(blank=True, null=True)
    rating = models.FloatField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title



class Episode(models.Model):
    movie = models.ForeignKey(Movie, related_name="episodes", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.movie.title} - {self.title}"


class Team(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='team_photos/')

    def __str__(self):
        return self.name


class Live(models.Model):
    team_1 = models.ForeignKey(Team, related_name='home_matches', on_delete=models.CASCADE)
    team_2 = models.ForeignKey(Team, related_name='away_matches', on_delete=models.CASCADE)
    link = models.URLField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Live Match"
        verbose_name_plural = "Live Matches"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.team_1} vs {self.team_2}"

    @property
    def photo_1(self):
        return self.team_1.photo

    @property
    def photo_2(self):
        return self.team_2.photo

