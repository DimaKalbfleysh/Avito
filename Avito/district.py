# coding=utf-8
from bs4 import BeautifulSoup
from Avito.request import Request


def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    elements = soup.find("optgroup", label="район").find_all("option")

    # Ключём является название района на русском, значение является название района на английском.
    data = {element.text: element.get("value") for element in elements}
    return data


def get_dict_district(city, list_ip):
    """ Функция возвращает словарь с районами city. """
    url = "https://avito.ru/{}".format(city)
    request = Request(url, list_ip)
    html = request.get_html()
    district = get_data(html)
    print(district)
    return district