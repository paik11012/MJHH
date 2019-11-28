from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Movie, Genre, User, Comment
User = get_user_model()
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content', 'score', 'movie_id', 'user_id']

class MovieSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)
    class Meta:
        model = Movie
        fields = ['id','title', 'poster_url', 'director', 'actor', 'description', 'grade', 'running_time', 'naver_score', 'open_date', 'audience', 'genre', 'liked_users', 'comments']

class MovieUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id','title', 'poster_url', 'director', 'actor', 'description', 'grade', 'running_time', 'naver_score', 'open_date', 'audience', 'genre', 'liked_users']

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name', ]

class GenreDetailSerializer(GenreSerializer):
    movie = MovieSerializer(many=True)
    class Meta(GenreSerializer.Meta):
        fields = GenreSerializer.Meta.fields + ['movie', ]

class UserDetailSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)
    liked_movies = MovieSerializer(many=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'followers', 'comments', 'liked_movies', ]
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', ]