from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.movies, name='movies'),
    path('movies_list', views.movies_list, name='movies_list'),
    path('<movie_id>', views.movie_single, name='movie_single'),
    path('movie/<int:movie_id>/add_comment/', views.add_review, name='add_review'),
    # path('/all_movies_list', views.particular_movie_page),
]
