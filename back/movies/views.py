from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from decouple import config
import time


# def update(request):
    # BASE_URL = 'https://openapi.naver.com/v1/search/movie.json'
    # CLIENT_ID = config('CLIENT_ID')
    # CLIENT_SECRET = config('CLIENT_SECRET')
    # HEADERS = {
    #     "X-Naver-Client-Id": CLIENT_ID,
    #     "X-Naver-Client-Secret": CLIENT_SECRET,
    # }
    # with open('movie.csv','r',newline='',encoding='utf8') as f:
    #     reader = csv.DictReader(f)
    #     with open('movie_naver.csv','w',newline='',encoding='utf-8') as fs:
    #         fieldnames = ('movieCd', 'link')
    #         writer = csv.DictWriter(fs, fieldnames=fieldnames)
    #         writer.writeheader()  
    #         for movie_info in reader:
    #             mv = {}
    #             mv[movie_info['movieCd']] = movie_info['movieNm']
    #             query = movie_info['movieNm']
    #             API_URL = f'{BASE_URL}?query={query}'
    #             time.sleep(0.05)
    #             response = requests.get(API_URL,headers=HEADERS).json()
    #             datas = response['items'][0]
    #             movieinfo = {
    #                 'movieCd' : movie_info['movieCd'],
    #                 'link' : datas['link'],
    # }
    #             writer.writerow(movieinfo)
