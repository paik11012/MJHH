from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# moive - title, poster_url, director, actor, description, grade, running_time, open_date, genre, user (edited) 
# user - follower, following
# genre - name

class User(AbstractUser):
    followers = models.ManyToManyField(  # 유저에게는 follower라는 필드가 있다, 내가 여러 명 팔로워 가능, 팔로잉 가능(모델끼리)
        settings.AUTH_USER_MODEL,
        related_name='followings'  # 팔로잉하는 사람들 가져오기 user.followings
    )
    liked_genres = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_users')


class Genre(models.Model):
    name = models.CharField(max_length=50)
    


class Movie(models.Model):
    title = models.CharField(max_length=50)
    poster_url = models.TextField()
    director = models.CharField(max_length=50)
    actor = models.CharField(max_length=50)
    description = models.TextField()
    grade = models.CharField(max_length=50)
    running_time = models.IntegerField()
    naver_score = models.FloatField()
    open_date = models.DateField()
    audience = models.IntegerField()
    genre = models.ForeignKey(Genre, related_name="movie", on_delete=models.CASCADE)
    liked_users =  models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_movies', blank=True)  # user model과 m:n관계 형성
    def __str__(self):
        return self.title

# comment
class Comment(models.Model):
    content = models.CharField(max_length=200)
    score = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="comments", on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name="comments", on_delete=models.CASCADE)
