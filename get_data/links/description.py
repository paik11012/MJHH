
from bs4 import BeautifulSoup
from urllib.request import urlopen
from pprint import pprint
import re

# with open('movie_naver.csv', 'r', newline='', encoding='utf-8') as f:
#     reader = csv.DictReader(f)
#     for row in reader:
url = 'https://movie.naver.com/movie/bi/mi/basic.nhn?code=163831'
html = urlopen(url)
source = html.read()
html.close()
soup = BeautifulSoup(source, 'html.parser')
# print(soup)
description = soup.select_one('p.con_tx').text

with open('test.txt', 'w', encoding='utf-8') as f :
    f.write(description)

print(description)
