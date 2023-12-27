from pprint import pprint

import requests
from bs4 import BeautifulSoup
from connect_mongo_db import mongo_save, connect_mongo_db, get_all_link, connect_mongo_collection
import time

"""Блок подключения к вебсайту извлечения ссылок на статьи и загрузки в монго"""


def parse_link():
    for p in range(5):
        # Получение ссылок на станицы где есть статьи
        url = f'https://sibac.info/arhive-article?page={p}'  # Динамически переключаю стрницы циклом
        r = requests.get(url)  # Запрос к нужной странице
        soup = BeautifulSoup(r.text, 'lxml')  # библиотека и парсер
        link_article = soup.find('div', id='archive-wrapp')  # Получаю ДИВ в ктором лежат 15 статей на одной странице
        for link in link_article:  # Пробегаемся по 15 статьям
            link = 'https://sibac.info/' + link.find('a').get(
                'href')  # Ищу иерархически ссылу и добавляю к ней домен сайта
            article_link_id = link[-6:]
            if connect_mongo_collection("link").find_one({f"doc.{article_link_id}": {"$exists": True}}):
                continue  # если в базе есть такая ссылка пропускаем
            else:
                mongo_save('doc', article_link_id, link=link)  # Сохраняем в монго
                print(f'{article_link_id} Такой записи нет в базе, сохраняю')


parse_link()

""" Получаю каждую  ссылку с монго,  перехожу в нее и запускаю новый парсер на статью """


def parse_article():
    links = get_all_link()
    for i in range(len(links)):
        url = links[i]
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')
        article = soup.find('div', class_='field-item even').findAll('p')
        for index, strong in enumerate(article, 0):
            if strong.text == 'АННОТАЦИЯ' or strong.text == 'Введение.':
                start_index = index
            elif strong.text == 'Список литературы:':
                stop_index = index
        article_list = []
        for art_elem in range(start_index, stop_index):
            article = soup.find('div', class_='field-item even').findAll('p')[art_elem].text
            article_list.append(article)
        article_list = ' '.join(article_list)
        connect_mongo_collection("article").insert_one({"article": article_list})
        print(article_list)
parse_article()
