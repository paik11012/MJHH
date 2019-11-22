import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

f = open('movie_naver.csv', 'r', encoding='utf-8')
csv_file = csv.reader(f)
for line in csv_file:
    one_line = str(line[1])
    # print(one_line)
    nums = one_line.split('=')
    naver_code = nums[1]
    base_image_url = 'https://movie.naver.com/movie/bi/mi/photoViewPopup.nhn?movieCode='
    total_image_url = base_image_url + naver_code
    response = requests.get(total_image_url)
    new = response.text
    soup = BeautifulSoup(new, 'html.parser')
    img = str(soup.select('img')[0])
    final = img.split('src=')
    final_url = final[-1]
    final_url = final_url[1:-3]
    print(final_url)
f.close
