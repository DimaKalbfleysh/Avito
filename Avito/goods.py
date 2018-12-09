# coding=utf-8
from bs4 import BeautifulSoup
from Avito.request import Request


def get_links_goods(html):
    soup = BeautifulSoup(html, "lxml")
    elements = soup.find_all("button", class_="js-item-extended-contacts item-extended-contacts button button-origin button-origin_small")
    links = ["https://avito.ru" + element.get("data-item-url") for element in elements]
    return links


def get_goods(urls, ip):
    """ Функция возвращает список ссылок на товары. """
    list_goods = []
    for url in urls:
        request = Request(url, ip)
        html = request.get_html()
        links = get_links_goods(html)
        list_goods.extend(links)
    return list_goods
