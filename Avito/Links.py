# coding=utf-8
from bs4 import BeautifulSoup
from Avito.Request import Request

urls = []


def get_last_page(html):
    try:
        soup = BeautifulSoup(html, "lxml")
        pages = soup.find("div", class_="pagination-pages clearfix").find_all("a", class_="pagination-page")
        page = pages[-1].get("href").split("?")[1].split("&")[0].split("=")[1]
        return page
    except:
        return 1


def get_links(city, categories, subcategories, district, ip, qq):
    for subcategory in subcategories:
        url = "https://avito.ru/{}/{}/{}?p={}&{}={}".format(city, categories, subcategory, 1, qq, district)
        n = int(get_last_page(Request(url, ip).getHtml()))
        print(n)
        for page in range(1, n + 1):
            url = "https://avito.ru/{}/{}/{}?p={}&{}={}".format(city, categories, subcategory, page, qq, district)
            url = Request(url, ip).getHtml("url")
            urls.append(url)
            print(url)


def links_to_product_pages(city, categories, subcategories, districts, ip, qq):
    """ Функция возвращает список ссылок страниц с товарими. """
    if type(districts) == dict:
        for district in districts:
            get_links(city, categories, subcategories, districts[district], ip, qq)
    else:
        get_links(city, categories, subcategories, districts, ip, qq)
    return urls
