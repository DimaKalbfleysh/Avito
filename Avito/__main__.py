# coding=utf-8
from Avito.District import getDistrict
from Avito.City import cities
from Avito.Links import linksToProductPages
from Avito.Goods import getGoods
from Avito.Category import getDictCategories
from Avito.NumberTelephone import getNumberTelephone
from Avito.Subcategories import getSubcategories
from Avito.Metro import getMetro
from Avito.Proxies import getProxy


def main():
    proxy_list = getProxy()

    categories = getDictCategories(proxy_list)

    city = cities["Ижевск"]

    district = getDistrict(city, proxy_list)

    # Если в city метро, а не районы, то
    # metro = getMetro(city, proxy_list)
    # Получаем словарь с метро city.

    category = categories["Велосипеды"]

    subcategories = getSubcategories(category, proxy_list)

    links_to_product_pages = linksToProductPages(city, category, subcategories, district['Октябрьский'], proxy_list, "district")

    goods = getGoods(links_to_product_pages, proxy_list)

    # Колличество потоков
    n = 5

    numbers = getNumberTelephone(goods, n)


if __name__ == '__main__':
    main()
