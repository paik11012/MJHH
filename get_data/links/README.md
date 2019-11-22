



## Movie data url을 csv로 가져오기

1. movie2.csv는 영화진흥위원회에서 가져온 52주 주말동안의 TOP 10 박스오피스 데이터입니다. 주간까지 하면 데이터가 너무 많기에 주말만 가져오는 것으로 설정해 데이터를 가져왔습니다. 
2. 가져온 movie2.csv를 바탕으로 네이버 영화 검색 API를 통해 추가적인 데이터를 수집했습니다. movie code와 link를 수집해 향후 데이터를 크롤링에 활용할 것 입니다. 가져온 데이터는 movie_naver.csv폴더에 저장했습니다. 

데이터를 가져오는 데 오류가 생겨 

```python
import requests
from pprint import pprint
from decouple import config
import time  # using time.sleep
import csv
BASE_URL = 'https://openapi.naver.com/v1/search/movie.json'
CLIENT_ID = config('CLIENT_ID')
CLIENT_SECRET = config('CLIENT_SECRET')
HEADERS = {
    "X-Naver-Client-Id": CLIENT_ID,
    "X-Naver-Client-Secret": CLIENT_SECRET,}
with open('movie.csv','r',newline='',encoding='utf8') as f:
    reader = csv.DictReader(f)
    with open('movie_naver.csv','w',newline='',encoding='utf-8') as fs:
        fieldnames = ('movieCd', 'link', 'image', 'userRating')
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
                'image' : datas['image'],
                'userRating' : datas['userRating'],}
            writer.writerow(movieinfo)
```

이미 만들었던 movie.csv파일 중 영화제목을 이용해서 네이버 영화 검색 api에서 영화 정보를 검색한다. 영화제목과 유인한 값인 영화코드를 이용해 dictionary를 만든다.  -> mv[movie_info['movieCd']] = movie_info['movieNm']
