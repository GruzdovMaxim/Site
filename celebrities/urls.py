from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.celebrities, name='celebrities'),
    path('/celebrities_list', views.celebrities_list, name='celebrities_list'),
    path('/<celebrities_id>', views.celebrities_single, name='celebrities_single'),

]
