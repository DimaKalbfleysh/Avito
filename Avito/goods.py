# coding=utf-8
from bs4 import BeautifulSoup
from Avito.request import Request

goods = []


def get_links_goods(html):
    soup = BeautifulSoup(html, "lxml")
    lists = soup.find_all("button", class_="js-item-extended-contacts item-extended-contacts button button-origin button-origin_small")
    links = ["https://avito.ru" + list.get("data-item-url") for list in lists]
    goods.extend(links)
    print(len(goods))


def get_goods(urls, ip):
    """ Функция возвращает список ссылок товаров. """
    for url in urls:
        html = Request(url, ip).get_html()
        get_links_goods(html)
    return goods
