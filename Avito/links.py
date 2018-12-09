# coding=utf-8
from bs4 import BeautifulSoup
from Avito.request import get_html

urls = []


def get_last_page(html):
    soup = BeautifulSoup(html, "lxml")
    try:
        pages = soup.find("div", class_="pagination-pages clearfix").find_all("a", class_="pagination-page")
    except AttributeError:
        return 1
    page = pages[-1].get("href").split("?")[1].split("&")[0].split("=")[1]
    return page


def get_links(city, categories, subcategories, direction, list_ip, district_or_metro):
    for subcategory in subcategories:
        args = [city, categories, subcategory, 1, district_or_metro, direction]
        url = "https://avito.ru/{}/{}/{}?p={}&{}={}".format(*args)
        html = get_html(url, list_ip)
        last_page = int(get_last_page(html))
        for page in range(1, last_page + 1):
            args[3] = page
            url = "https://avito.ru/{}/{}/{}?p={}&{}={}".format(*args)
            urls.append(url)


def links_to_product_pages(city, categories, subcategories, direction, list_ip, district_or_metro):
    """ Функция возвращает список ссылок на страницы с товарими. """
    if type(direction) == dict:
        for i in direction:
            get_links(city, categories, subcategories, direction[i], list_ip, district_or_metro)
        return urls
    get_links(city, categories, subcategories, direction, list_ip, district_or_metro)
    return urls

