from django.db import models
from movies.models import TheMovie
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class MovieDBUser(models.Model):
    nick_name = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    email_address = models.EmailField(max_length=30)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    avatar_icon = models.BinaryField()
    avatar_icon_changed = models.BooleanField()
    favourite_movies = models.ManyToManyField(TheMovie)

    def __str__(self):
        return self.nick_name


class MovieReview(models.Model):
    title = models.CharField(max_length=50)
    main_text = models.CharField(max_length=10000)
    movie_rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    the_movie = models.ForeignKey(TheMovie, on_delete=models.PROTECT)
    the_user = models.ForeignKey(MovieDBUser, on_delete=models.PROTECT)
    is_created_at = models.DateField()

    def __str__(self):
        return self.title
