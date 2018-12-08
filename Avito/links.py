# coding=utf-8
from bs4 import BeautifulSoup
from Avito.request import Request

urls = []


def get_last_page(html):
    soup = BeautifulSoup(html, "lxml")
    try:
        pages = soup.find("div", class_="pagination-pages clearfix").find_all("a", class_="pagination-page")
    except AttributeError:
        return 1
    page = pages[-1].get("href").split("?")[1].split("&")[0].split("=")[1]
    return page


def get_links(city, categories, subcategories, district, list_ip, district_or_metro):
    for subcategory in subcategories:
        args = [city, categories, subcategory, 1, district_or_metro, district]
        url = "https://avito.ru/{}/{}/{}?p={}&{}={}".format(*args)
        request = Request(url, list_ip)
        html = request.get_html()
        last_page = int(get_last_page(html))
        print(last_page)
        for page in range(1, last_page + 1):
            args[3] = page
            url = "https://avito.ru/{}/{}/{}?p={}&{}={}".format(*args)
            print(url)
            urls.append(url)


def links_to_product_pages(city, categories, subcategories, districts, ip, district_or_metro):
    """ Функция возвращает список ссылок страниц с товарими. """
    if type(districts) == dict:
        for district in districts:
            get_links(city, categories, subcategories, districts[district], ip, district_or_metro)
    else: get_links(city, categories, subcategories, districts, ip, district_or_metro)
    return urls
