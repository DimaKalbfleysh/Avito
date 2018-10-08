# coding=utf-8
from bs4 import BeautifulSoup
from Avito.Request import Request


def getData(html):
    data = {}
    soup = BeautifulSoup(html, "lxml")
    tds = soup.find("optgroup", label="район").find_all("option")
    for td in tds:
        name = td.text
        id = td.get("value")
        data[name] = id
    return data


def getDistrict(city, ip):
    """ Функция возвращает словарь с районами city.
    Ключём является название района на русском,
    значение является название района на английском. """

    url = "https://avito.ru/{}".format(city)
    district = getData(Request(url, ip).getHtml())
    print(district)
    return district
