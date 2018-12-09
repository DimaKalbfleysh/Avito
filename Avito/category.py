# coding=utf-8
from bs4 import BeautifulSoup

from Avito.request import get_html
from Avito.categories import categories


def get_list_categories(html):
    """ Функция возвращает список категорий. """
    soup = BeautifulSoup(html, 'lxml')
    elements = soup.find('nav', class_='category-map').find_all('li', class_='category-map-item')
    links = [element.find('a').get('href').split("/")[2] for element in elements]
    return links


def get_dict_categories(list_ip):
    """ Функция возвращает словарь с категориями. """
    html = get_html('https://www.avito.ru/', list_ip)
    links = get_list_categories(html)

    # Добавляем в словарь категории. Ключём является название категории на русском языке,
    # значение является название категории на английском языке
    dict_categories = {category: links[categories.index(category)] for category in categories}
    return dict_categories
