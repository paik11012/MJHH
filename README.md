# 영화 추천 서비스



## 11.22

시리얼라이저 만들기

```python
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Movie, Genre, User, Comment
User = get_user_model()
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content', 'score', 'movie_id', 'user_id']
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id','title', 'poster_url', 'director', 'actor', 'description', 'grade', 'running_time', 'naver_score', 'open_date', 'audience', 'genre', 'liked_users', ]
class MovieUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id','title', 'poster_url', 'director', 'actor', 'description', 'grade', 'running_time', 'naver_score', 'open_date', 'audience', 'genre']
class MovieDetailSerializer(MovieSerializer):
    comment = CommentSerializer(many=True)
    class Meta(MovieSerializer.Meta):
        fields = MovieSerializer.Meta.fields + ['comment', ]
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
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'followers', 'comments', ]
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', ]
```

modles.py 만들기

```python
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

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
    liked_users =  models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_movies')  # user model과 m:n관계 형성
    def __str__(self):
        return self.title
        
# comment
class Comment(models.Model):
    content = models.CharField(max_length=200)
    score = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="comments", on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name="comments", on_delete=models.CASCADE)
```

settings.py설정, 엄청난 installed apps

```
INSTALLED_APPS = [
    'movies',
    
    'rest_framework',
    'corsheaders',
    'rest_auth',
    'rest_auth.registration',
    'allauth',
    'allauth.account',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

## 11.25

영화진흥위원회 API와 네이버 영화 API를 통해 필요한 정보를 다 받아서 저장하는 views.py의 함수를 정의했다. 진짜 길다.

현재로부터 52주간 주말 데이터를 불러왔다. 영진위에서 movieCd(영화코드)를 받아오고 이를 네이버에서 제공하는 영화코드와 비교했다. 네이버 코드를 통해 이미지가 있는 네이버 링크와  description을 불러오고 다른 모든 정보를 받아왔다.  

movies = {}라는 딕셔너리를 만들어 그곳에 모든 정보를 넣고 맨 아래코드로 각 정보를 매칭했다.

```python
def update(request):
    # 영진위 코드
    baseurl = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json'
    movies = {}
    NAVER_URL = 'https://openapi.naver.com/v1/search/movie.json'
    CLIENT_ID = config('CLIENT_ID')
    CLIENT_SECRET = config('CLIENT_SECRET')
    HEADERS = {
        "X-Naver-Client-Id": CLIENT_ID,
        "X-Naver-Client-Secret": CLIENT_SECRET,
        }
    all_movies = Movie.objects.all()
    for da in range(52): 
        targetDt = datetime(2019, 11, 23) - timedelta(weeks=da)
        targetDt = targetDt.strftime('%Y%m%d')
        key = config('API_KEY')                 
        api_url = f'{baseurl}?key={key}&targetDt={targetDt}&weekGb=1'
        response = requests.get(api_url).json()
        for value in response.get('boxOfficeResult').get('weeklyBoxOfficeList'):
            flag = 0
            if movies.get(value['movieCd']) == None:
                for i in range(len(all_movies)):
                    if str(all_movies[i]) == value['movieNm']:
                        flag = 1
                        break
                if flag == 0:
                    movies[value['movieCd']] = [value['movieNm'], value['audiAcc'], value['openDt']]
    # naver
    for moviecode in movies.keys():
        try:
            query = movies[moviecode][0]
            API_URL = f'{NAVER_URL}?query={query}'
            time.sleep(0.05)
            response_naver = requests.get(API_URL,headers=HEADERS).json()
            datas = response_naver['items'][0]

            # image
            naver_code = datas['link']
            naver_code = naver_code.split('=')[1]
            image_url = f'https://movie.naver.com/movie/bi/mi/photoViewPopup.nhn?movieCode={naver_code}'
            response = requests.get(image_url)
            new = response.text
            soup = BeautifulSoup(new, 'html.parser')
            img = str(soup.select('img')[0])
            final = img.split('src=')
            final_url = final[-1]
            final_url = final_url[1:-3]

            # description
            des = datas['link']
            html = urlopen(des)
            source = html.read()
            html.close()
            soup = BeautifulSoup(source, 'html.parser')
            description = soup.find('p', class_='con_tx')
            step = soup.find('dl', 'info_spec')
            genre = step.find('a').text
            genre_name = {'드라마':1, '판타지':2, '서부':3, '공포':4, '로맨스':5, '모험':6, '스릴러':7, '느와르':8, '컬트':9, '다큐멘터리':10, '코미디':11, '가족':12, '미스터리':13, '전쟁':14, '애니메이션':15, '범죄':16, '뮤지컬':17, 'SF':18, '액션':19, '무협':20, '에로': 21, '서스펜스':22, '서사':23, '블랙코미디':24, '실험':25, '영화카툰':26, '영화음악':27, '영화패러디포스터':28, '멜로/로맨스':29}
            grade = step.find_all('dd')[3].find('a').text
            running = int(step.find('dd').find_all('span')[2].text[:-2])
            movies[moviecode].extend([datas['director'], datas['actor'], datas['userRating'], final_url, description.get_text(), genre_name.get(genre), grade, running])
            movie = Movie()
            movie.title = movies[moviecode][0]
            movie.audience = movies[moviecode][1]
            movie.open_date = movies[moviecode][2]
            movie.director = movies[moviecode][3]
            movie.actor = movies[moviecode][4]
            movie.naver_score = movies[moviecode][5]
            movie.poster_url = movies[moviecode][6]
            movie.description = movies[moviecode][7]
            movie.genre = get_object_or_404(Genre, pk=movies[moviecode][8])
            movie.grade = movies[moviecode][9]
            movie.running_time = movies[moviecode][10]
            movie.save()
        except:
            print('error')
```





## 11.27

부트스트랩 적용

영화 5개 보이게 하기

디테일 페이지 만들기



like, comment 기능 구현(detail에)

nav bar만들기

검색기능 만들기

## 11.28

디테일 페이지에 코멘트 구현하기

로그인 후 마이페이지 들어가게

추천 알고리즘 적용하기

admin은 회원정보 수정 삭제 가능

