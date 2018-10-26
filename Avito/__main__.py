# coding=utf-8
from Avito.District import get_district
from Avito.City import cities
from Avito.Links import links_to_product_pages
from Avito.Goods import get_goods
from Avito.Category import get_dict_categories
from Avito.NumberTelephone import get_number_telephone
from Avito.Subcategories import get_subcategories
from Avito.Metro import getMetro
from Avito.Proxies import get_proxy


def main():
    proxy_list = get_proxy()

    categories = get_dict_categories(proxy_list)

    city = cities["Ижевск"]

    district = get_district(city, proxy_list)

    # Если в city метро, а не районы, то
    # metro = getMetro(city, proxy_list)
    # Получаем словарь с метро city.

    category = categories["Велосипеды"]

    subcategories = get_subcategories(category, proxy_list)

    links_to_product_pages = links_to_product_pages(city, category, subcategories, district['Октябрьский'], proxy_list, "district")

    goods = get_goods(links_to_product_pages, proxy_list)

    # Колличество потоков
    n = 5

    numbers = get_number_telephone(goods, n)


if __name__ == '__main__':
    main()
