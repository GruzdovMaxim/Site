from django.db import models
from django.core.validators import MinValueValidator


# Create your models here.
class Actor(models.Model):
    full_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    country = models.CharField(max_length=20)
    height = models.IntegerField(validators=[MinValueValidator(0.0)])
    directory_name = models.CharField(max_length=20)
    short_description = models.CharField(max_length=2000)
    biography = models.CharField(max_length=20000)

    def __str__(self):
        return self.full_name
