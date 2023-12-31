from pprint import pprint
import json
import requests
from bs4 import BeautifulSoup


def parse_link():
    data_link = []
    for p in range(4):
        # Получение ссылок на станицы где есть статьи
        url = f'https://sibac.info/arhive-article?page={p}'  # Динамически переключаю стрницы циклом
        r = requests.get(url)  # Запрос к нужной странице
        soup = BeautifulSoup(r.text, 'lxml')  # библиотека и парсер
        link_article = soup.find('div', id='archive-wrapp')  # Получаю ДИВ в ктором лежат 15 статей на одной странице
        for link in link_article:  # Пробегаемся по 15 статьям
            link = 'https://sibac.info/' + link.find('a').get(
                'href')  # Ищу иерархически ссылу и добавляю к ней домен сайта
            data_link.append({"link": link})
            print(f'На сайте найдена ссылка {link} сохранена в файле.')
        with open('data_link.json', 'w') as f:
            json.dump(data_link, f, indent=4)


def read_json_link():
    with open('data_link.json', 'r') as f:
        links = json.load(f)
        return links


def parse_article():
    links = read_json_link()
    with open('data_article.json', 'w', encoding='utf-8') as f:  # открываем файл для добавления
        for i in range(len(links)):
            url = links[i]['link']
            r = requests.get(url)
            soup = BeautifulSoup(r.text, 'lxml')
            article = soup.find('div', class_='field-item even').findAll('p')
            x = []
            for index, strong in enumerate(article, 0):
                if strong.text == 'АННОТАЦИЯ' or strong.text == 'Введение.':
                    start_index = index
                    x.append(start_index)
                elif strong.text == 'Список литературы:':
                    stop_index = index
                    x.append(stop_index)
            if not x or len(x) != 2:
                continue
            else:
                data_article = []
                b = []
                for i in range(x[0], x[1]):
                    article = soup.find('div', class_='field-item even').findAll('p')[i].text
                    data_article.append(article)
                    t = ' '.join(data_article)
                b.append({"article": t})
                for i in b:
                    print(i)
                    json.dump(i, f, ensure_ascii=False, indent=4)  # записываем статью в файл


parse_link()
parse_article()
