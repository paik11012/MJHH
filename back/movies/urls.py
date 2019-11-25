from django.urls import path, include
from . import views

urlpatterns = [
    path('movielist/', views.movielist),
    path('update/', views.update),
    path('create/', views.create),
    path('moviedetail/<int:movie_pk>/', views.moviedetail),
    path('genrelist/', views.genrelist),
    path('genredetail/<int:genre_pk>/', views.genredetail),
    path('commentcreate/<int:movie_pk>/', views.commentcreate),
    path('comment_update_and_delete/<int:comment_pk>', views.comment_update_and_delete),
    # path('delete/', views.delete),
]