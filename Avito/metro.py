# coding=utf-8
from bs4 import BeautifulSoup
from Avito.request import get_html

city_with_metro = {"Москва": "moscow",
                   "Санкт-перербург": "spb"}


def get_data(html, label, tag, attribute):
    soup = BeautifulSoup(html, "lxml")
    if label:
        elements = soup.find("optgroup", label="метро")
    else:
        elements = soup.find("g")
    elements = elements.find_all(tag)
    data = {element.text: element.get(attribute) for element in elements}
    return data


def get_metro(city, list_ip):
    if city in city_with_metro:
        url = "https://www.avito.ru/s/avito/components/metro-map/svg-maps/metro-map-{}.svg".format(
            city_with_metro[city])
        html = get_html(url, list_ip)
        name = get_data(html, False, "text", "data-st-id")
        return name
    else:
        url = "https://www.avito.ru/{}".format(city)
        html = get_html(url, list_ip)
        name = get_data(html, True, "option", "value")
        return name
