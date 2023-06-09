from django.urls import path, include

from . import views

# app_name = "users_app"

urlpatterns = [
    path('', views.user_profile, name='user_profile'),
    path('/password', views.user_profile_password, name='user_profile_password'),
    path('/user_add_favourite_movie/<selected_movie_id>', views.add_favourite_movie, name='user_add_favourite_movie'),
    path('/user_favorite_grid', views.user_favorite_grid, name='user_favorite_grid'),
    path('/user_favorite_list', views.user_favorite_list, name='user_favorite_list'),
    path('/user_registration', views.user_registration, name='user_registration'),
    path('/user_login', views.user_login, name='user_login'),
    path('/user_logout', views.user_logout, name='user_logout'),
    path('/user_change_avatar', views.user_change_avatar, name='user_change_avatar'),
]
