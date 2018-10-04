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
    # Получаем список прокси.

    categories = getDictCategories(proxy_list)
    # Получаем словарь с категориями.

    city = cities["Ижевск"]
    # Получаем нужный город

    district = getDistrict(city, proxy_list)
    # Получаем словарь с районами city.

    # Если в city метро, а не районы, то
    'metro = getMetro(city, proxy_list)'
    # Получаем словарь с метро в городе.

    category = categories["Велосипеды"]
    # Получаем нужную категорию

    subcategories = getSubcategories(category, proxy_list)
    # Получаем список подкатегорий category

    links_to_product_pages = linksToProductPages(city, category, subcategories, district['Октябрьский'], proxy_list, "district")
    # Получаем список ссылок страниц с товарими

    goods = getGoods(links_to_product_pages, proxy_list)
    # Получаем список ссылок товаров

    n = 5
    # n = колличество потоков

    number = getNumberTelephone(goods, n)
    # Получаем список номеров телефона продовцов


if __name__ == '__main__':
    main()
