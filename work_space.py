import requests
from bs4 import BeautifulSoup
from connect_mongo_db import mongo_save, connect_mongo_db, get_one_link

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
    links = get_one_link()
    print(links[0])


parse_article()
