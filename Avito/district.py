# coding=utf-8
from bs4 import BeautifulSoup
from Avito.request import get_html


def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    elements = soup.find("optgroup", label="район").find_all("option")
    # Ключём является название района на русском, значение является id района.
    data = {element.text: element.get("value") for element in elements}
    return data


def get_dict_district(city, list_ip):
    """ Функция возвращает словарь с районами city. """
    url = "https://avito.ru/{}".format(city)
    html = get_html(url, list_ip)
    district = get_data(html)
    return district
