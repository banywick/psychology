import requests
from bs4 import BeautifulSoup
from connect_mongo_db import mongo_save, get_one_link

"""Блок подключения к вебсайту извлечения ссылок на статьи и загрузки в монго"""

data = []
for p in range(1):
    # Получение ссылок на станицы где есть статьи
    url = f'https://sibac.info/arhive-article?page={p}'  # Динамически переключаю стрницы циклом
    r = requests.get(url)  # Запрос к нужной странице
    soup = BeautifulSoup(r.text, 'lxml') #библиотека и парсер
    link_article = soup.find('div', id='archive-wrapp')  # Получаю ДИВ в ктором лежат 15 статей на одной странице
    for id, link in enumerate(link_article, 1):
        link = 'https://sibac.info/' + link.find('a').get('href')  # Ищу иерархически ссылу и добавляю к ней домен сайта
        # mongo_save('doc', id, link=link)
        # print(f'Записано {id}')
# print(f'Количество ссылок для обработки - {len(data)}')

""" Получаю первую ссылку переходу в нее и запускаю новый парсер на статью"""
print(get_one_link())





