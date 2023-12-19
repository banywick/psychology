import requests
from bs4 import BeautifulSoup


"""Блок подключения к вебсайту извлечения ссылок на статьи и помещение их в список"""

data = []
# for p in range(1):
#     # Получение ссылок на станицы где есть статьи
#     url = f'https://sibac.info/arhive-article?page={p}'  # Динамически переключаю стрницы циклом
#     r = requests.get(url)  # Запрос к нужной странице
#     soup = BeautifulSoup(r.text, 'lxml')
#     link_article = soup.find('div', id='archive-wrapp')  # Получаю ДИВ в ктором лежат 15 статей на одной странице
#     for link in link_article:
#         link = 'https://sibac.info/' + link.find('a').get('href')  # Ищу иерархически ссылу и добавляю к ней домен сайта
#         data.append(link)  # Записываю полноценные ссылки в список.
# print(f'Количество ссылок для обработки - {len(data)}')

""" Далее блок извлечения ссылок из списка переход на их страницу и извлечение статей """

print(data)

