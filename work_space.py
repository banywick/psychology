import requests
from bs4 import BeautifulSoup

count = 0

for p in range(2):

    # Получение ссылок на станицы где есть статьи
    url = f'https://sibac.info/arhive-article?page={p}'

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    # link_article = soup.find('div', id='archive-wrapp').find('div', class_='item').find('p').find('a').get('href')
    link_article = soup.find('div', id='archive-wrapp')

    data = []

    for link in link_article:
        link = 'https://sibac.info/' + link.find('a').get('href')
        data.append(link)
        count += 1
        print(count, link)
    # print(data)
