from urllib import request

def fetch_url(url):
  opener = request.build_opener()
  opener.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0')]
  request.install_opener(opener)
  html_string = request.urlopen(url).read()
  return html_string.decode()
#print(fetch_url('https://www.imdb.com/list/ls055386972/'))
import csv, re
from bs4 import BeautifulSoup

title_url = 'https://www.imdb.com/list/ls055386972/'
title_html = fetch_url(title_url)
title_soup = BeautifulSoup(title_html)

# opening a file and creating new csv writer object
out_file = open('filmy_imdb.csv', 'w', encoding='utf-8')
out_csv = csv.writer(out_file)
#write header row
out_csv.writerow(['Title', 'Genre', 'Director', 'Time'])

film_content = title_soup.find_all('div', {'class': 'lister-item-content'})
for title_info in film_content:
  title_name = title_info.find('a').text.strip()
  film_time = title_info.find('span', {'class': 'runtime'}).text.strip()
  film_genre= title_info.find('span', {'class': 'genre'}).text.strip()
  film_director = title_info.find(href=re.compile('name')).text.strip()

  print (title_name + ' '+ film_genre+ ' '+ film_director+' '+ film_time)
  out_csv.writerow([title_name, film_genre, film_director, film_time])


out_file.close()