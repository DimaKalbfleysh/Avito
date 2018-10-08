# coding=utf-8
from bs4 import BeautifulSoup
from Avito.Request import Request

city_with_metro = {"Москва": "moscow",
                   "Санкт-перербург": "spb"}


def getData(html, label, tag, attribute):
    data = {}
    soup = BeautifulSoup(html, "lxml")
    if label:
        names = soup.find("optgroup", label="метро")
    else:
        names = soup.find("g")
    names = names.find_all(tag)
    for name in names:
        id = name.get(attribute)
        name = name.text
        data[name] = id
    return data


def getMetro(city, ip):
    if city in city_with_metro:
        url = "https://www.avito.ru/s/avito/components/metro-map/svg-maps/metro-map-{}.svg".format(
            city_with_metro[city])
        html = Request(url, ip).forMetro()
        name = getData(html, False, "text", "data-st-id")
        return name
    else:
        html = Request("https://www.avito.ru/{}".format(city), ip).getHtml()
        name = getData(html, True, "option", "value")
        return name
