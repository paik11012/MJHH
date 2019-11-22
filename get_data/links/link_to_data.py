# 비로그인 오픈 API이므로 GET으로 호출할 때 HTTP Header에 애플리케이션 등록 시 발급받은 Client ID와 Client Secret 값을 같이 전송해 주시면 활용 가능
from pprint import pprint
from bs4 import BeautifulSoup
from urllib.request import urlopen
import json
import csv

f = open('movie_naver.csv', 'r', encoding='utf-8')
csv_file = csv.reader(f)
for line in csv_file:
    one_line = str(line[1])
    nums = one_line.split('=')
    naver_code = nums[1]
    base_image_url = 'https://movie.naver.com/movie/bi/mi/photoViewPopup.nhn?movieCode='
    total_image_url = base_image_url + naver_code
    print(total_image_url)
f.close
