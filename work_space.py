from pprint import pprint

import requests
from bs4 import BeautifulSoup
from connect_mongo_db import mongo_save, connect_mongo_db, get_all_link
import time

"""Блок подключения к вебсайту извлечения ссылок на статьи и загрузки в монго"""


def parse_link():
    for p in range(1):
        # Получение ссылок на станицы где есть статьи
        url = f'https://sibac.info/arhive-article?page={p}'  # Динамически переключаю стрницы циклом
        r = requests.get(url)  # Запрос к нужной странице
        soup = BeautifulSoup(r.text, 'lxml')  # библиотека и парсер
        link_article = soup.find('div', id='archive-wrapp')  # Получаю ДИВ в ктором лежат 15 статей на одной странице
        for link in link_article:  # Пробегаемся по 15 статьям
            link = 'https://sibac.info/' + link.find('a').get(
                'href')  # Ищу иерархически ссылу и добавляю к ней домен сайта
            article_link_id = link[-6:]
            if connect_mongo_db().find_one({f"doc.{article_link_id}": {"$exists": True}}):
                continue  # если в базе есть такая ссылка пропускаем
            else:
                mongo_save('doc', article_link_id, link=link)  # Сохраняем в монго
                print(f'{article_link_id} Такой записи нет в базе, сохраняю')


# parse_link()

""" Получаю первую ссылку перехожу в нее и запускаю новый парсер на статью"""


def parse_article():
    article_list = []
    links = get_all_link()
    for i in range(5, 8):
        url = links[i]
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')
        article = soup.find('div', class_='field-item even').findAll('p')

        for index, strong in enumerate(article, 0):
            if strong.text == 'АННОТАЦИЯ' or strong.text == 'Введение.':
                start_index = index


            elif strong.text == 'Список литературы:':
                stop_index = index


        for art_elem in range(start_index, stop_index):
            soup = BeautifulSoup(r.text, 'lxml')
            article = soup.find('div', class_='field-item even').findAll('p')[art_elem].text
            article_list.append(article)
        print(article_list)


parse_article()
