# coding=utf-8
from bs4 import BeautifulSoup
from Avito.Request import Request

links = []


def getLinksGoods(html):
    soup = BeautifulSoup(html, "lxml")
    tds = soup.find_all("div", class_="item item_table clearfix js-catalog-item-enum js-item-extended item_table_extended snippet-experiment item_hide-elements")
    for td in tds:
        try:
            try:
                href = "https://avito.ru" + td.find("a", class_="js-item-slider item-slider large-picture").get("href")
                links.append(href)
            except AttributeError:
                href = "https://avito.ru" + td.find("a", class_="photo-wrapper js-photo-wrapper large-picture").get("href")
                links.append(href)
        except AttributeError:
            href = "https://avito.ru" + td.find("a", class_="item-missing-photo").get("href")
            links.append(href)
    print(len(links))
    return links


def getGoods(urls, ip):
    """ Функция возвращает список ссылок товаров. """
    for url in urls:
        html = Request(url, ip).getHtml()
        getLinksGoods(html)
    return links



