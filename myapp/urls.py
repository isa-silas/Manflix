from django.urls import path

from .views import *

urlpatterns = [
    path("category/",CategoryAPIView.as_view(),name = "category"),
    path('category/<int:pk>/',CategoryAPIView.as_view(),name ='categoryParameters'),
    path("signature/",SignatureAPIView.as_view(),name = "signature"),
    path('signature/<int:pk>/',SignatureAPIView.as_view(),name ='signatureParameters'),
    path("users/",UsersAPIView.as_view(),name = "users"),
    path('users/<int:pk>/',UsersAPIView.as_view(),name ='usersParameters'),
    path("movies/",MoviesAPIView.as_view(),name = "movies"),
    path('movies/<int:pk>/',MoviesAPIView.as_view(),name ='moviesParameters'),
    path("favorite/",FavoriteAPIView.as_view(),name = "favorite"),
    path('favorite/<int:pk>/',FavoriteAPIView.as_view(),name ='favoriteParameters'),
]