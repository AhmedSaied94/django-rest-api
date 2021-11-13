from django.urls import path
from .views import *

app_name = 'entertainment'

urlpatterns = [
    path('movies', movies_list, name='movies'),
    path('movies/<int:pk>/details', movie_details, name='movie-details'),
    path('movies/create', movie_create, name='movie-create'),
    path('movies/<int:pk>/delete', movie_delete, name='movie-delete'),
    path('movies/<int:pk>/update', movie_update, name='movie-update')
]