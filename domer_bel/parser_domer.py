from pprint import pprint
from bs4 import BeautifulSoup
import requests

# Отправляем GET-запрос к сайту Хабр и получаем его HTML код
response = requests.get("https://xn--d1acuhm.xn--90ais/")
html = response.text

# Создаем объект BeautifulSoup, используя парсер lxml
soup = BeautifulSoup(html, "lxml")

# Получаем чистую разметку HTML документа
clean_html = soup.prettify()

# Выводим или сохраняем чистую разметку HTML
# print(clean_html)
# или
with open("clean_html.txt", "w", encoding="utf-8") as f:
    f.write(clean_html)

