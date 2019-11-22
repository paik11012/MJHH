# 비로그인 오픈 API이므로 GET으로 호출할 때 HTTP Header에 애플리케이션 등록 시 발급받은 Client ID와 Client Secret 값을 같이 전송해 주시면 활용 가능
import requests
from pprint import pprint
from decouple import config
import time
#포문 안에서
import csv
BASE_URL = 'https://openapi.naver.com/v1/search/movie.json'
CLIENT_ID = config('CLIENT_ID')
CLIENT_SECRET = config('CLIENT_SECRET')
HEADERS = {
    "X-Naver-Client-Id": CLIENT_ID,
    "X-Naver-Client-Secret": CLIENT_SECRET,}

with open('movie2.csv','r',newline='',encoding='utf8') as f:
    reader = csv.DictReader(f)
    with open('movie_naver.csv','w',newline='',encoding='utf-8') as fs:
        fieldnames = ('movieCd', 'link')
        writer = csv.DictWriter(fs, fieldnames=fieldnames)
        writer.writeheader()  
        for movie_info in reader:
            mv = {}
            mv[movie_info['movieCd']] = movie_info['movieNm']
            query = movie_info['movieNm']
            API_URL = f'{BASE_URL}?query={query}'
            time.sleep(0.05)
            response = requests.get(API_URL,headers=HEADERS).json()
            datas = response['items'][0]
            movieinfo = {
                'movieCd' : movie_info['movieCd'],
                'link' : datas['link'],
}
            writer.writerow(movieinfo)