# coding=utf-8
from Avito.district import get_dict_district
from Avito.city import cities
from Avito.links import links_to_product_pages
from Avito.goods import get_goods
from Avito.category import get_dict_categories
from Avito.number_telephone import get_number_telephone
from Avito.subcategories import get_subcategories
from Avito.metro import get_metro
from Avito.proxies import get_proxy


def main():
    list_ip = get_proxy()
    categories = get_dict_categories(list_ip)
    category = categories["Велосипеды"]
    city = cities["Ижевск"]
    district = get_dict_district(city, list_ip)

    # Если в city метро, а не районы, то
    # metro = get_metro(city, proxy_list)
    # Получаем словарь с метро city.
    district_or_metro = "district"
    subcategories = get_subcategories(category, list_ip)
    links = links_to_product_pages(city, category, subcategories, district['Октябрьский'], list_ip, district_or_metro)
    goods = get_goods(links, list_ip)
    # Колличество потоков
    n = 5
    numbers = get_number_telephone(goods, n)

if __name__ == '__main__':
    main()
