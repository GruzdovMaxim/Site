# Generated by Django 4.1.9 on 2023-06-09 01:30

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieDBUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick_name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=30)),
                ('email_address', models.EmailField(max_length=30)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('avatar_icon', models.FileField(upload_to='')),
                ('avatar_icon_changed', models.BooleanField()),
                ('favourite_movies', models.ManyToManyField(to='movies.themovie')),
            ],
        ),
        migrations.CreateModel(
            name='MovieReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('main_text', models.CharField(max_length=10000)),
                ('movie_rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('is_created_at', models.DateField()),
                ('the_movie', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='movies.themovie')),
                ('the_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.moviedbuser')),
            ],
        ),
    ]
