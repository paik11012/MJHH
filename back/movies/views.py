from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from datetime import datetime, timedelta
# from decouple import config
from pprint import pprint
from .models import Movie, Genre, Comment
from .serializers import MovieSerializer, GenreSerializer, CommentSerializer, UserDetailSerializer, GenreDetailSerializer, UserSerializer, UserDetailSerializer, MovieUpdateSerializer
import time
from django.contrib.auth import get_user_model


def update(request):
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

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
def moviedetail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = MovieUpdateSerializer(data=request.data, instance=movie)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    else:
        movie.delete()
        return Response({'message': '영화가 삭제되었습니다.'})


@api_view(['GET'])
@permission_classes([AllowAny])
def movielist(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)



    
@api_view(['POST'])
@permission_classes([AllowAny])
def create(request):
    serializer = MovieUpdateSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def genrelist(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def genredetail(request, genre_pk):
    genre = get_object_or_404(Genre, pk=genre_pk)
    if request.method == 'GET':
        serializer = GenreDetailSerializer(genre)
        return Response(serializer.data)

@api_view(['POST'])
@permission_classes([AllowAny])
def commentcreate(request, movie_pk):
    serializer = CommentSerializer(data=request.data)
    user_id = request.data.get('user_id')
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie_id=movie_pk, user_id=user_id)
    return Response(serializer.data)

@api_view(['PUT', 'DELETE'])
@permission_classes([AllowAny])
def comment_update_and_delete(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'PUT':
        serializer = CommentSerializer(data=request.data, instance=comment)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message': '코멘트가 수정되었습니다.'})
    else:
        comment.delete()
        return Response({'message': '코멘트가 삭제되었습니다.'})


@api_view(['GET'])
@permission_classes([AllowAny])
def userlist(request):
    users = get_user_model().objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def userdetail(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    serializer = UserDetailSerializer(user)
    return Response(serializer.data)
    