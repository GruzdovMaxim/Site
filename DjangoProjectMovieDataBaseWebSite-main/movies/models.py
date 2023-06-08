from django import forms
from django.db import models
from djongo.models import ArrayField
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class MovieGenre(models.Model):
    whole_name = models.CharField(max_length=20)
    background_color = models.CharField(max_length=15)
    wiki_link = models.CharField(max_length=100)

    def __str__(self):
        return self.whole_name


# class AdditionalMovieInfo(models.Model):
#     field_key = models.CharField(max_length=20)
#     field_value = models.CharField(max_length=20)
#
#     class Meta:
#         abstract = True


class TheMovie(models.Model):
    title = models.CharField(max_length=20)
    director = models.CharField(max_length=50)
    writer = models.CharField(max_length=50)
    # celebrities = models.CharField(max_length=50)
    genres = models.ManyToManyField(MovieGenre)
    release_date = models.DateField()
    duration = models.CharField(max_length=10)
    movie_score = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    MPAA_rating = models.CharField(max_length=10)
    # plot_keywords = ArrayField(model_container=AdditionalMovieInfo)
    directory_name = models.CharField(max_length=20)
    in_cinema = models.BooleanField()
    on_tv = models.BooleanField()

    def __str__(self):
        return self.title
