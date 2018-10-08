# coding=utf-8
from bs4 import BeautifulSoup
from Avito.Request import Request


def getData(html):
    links = []
    soup = BeautifulSoup(html, "lxml")
    tds = soup.find("div", class_="catalog-counts__section").find_all("li")
    for td in tds:
        href = td.find("a").get("href").split("/")[3].split("?")[0]
        links.append(href)
    return links


def getSubcategories(category, ip):
    """ Функция возвращает список подкатегорий category. """
    url = "https://avito.ru/rossiya/{}".format(category)
    while True:
        try:
            subcategories = getData(Request(url, ip).getHtml())
            print(subcategories)
            return subcategories
        except:
            continue
