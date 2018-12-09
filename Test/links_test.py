from Avito.category import get_dict_categories
from Avito.city import cities
from Avito.district import get_dict_district
from Avito.links import links_to_product_pages
from Avito.proxies import get_proxy
from Avito.subcategories import get_subcategories

list_ip = get_proxy()
categories = get_dict_categories(list_ip)
category = categories["Велосипеды"]
city = cities["Ижевск"]
direction = get_dict_district(city, list_ip)
district_or_metro = 'district'
# Если в city метро, а не районы, то
# metro = get_metro(city, proxy_list)
# Получаем словарь с метро city.

subcategories = get_subcategories(category, list_ip)

while 1:
    links = links_to_product_pages(city, category, subcategories, direction, list_ip, district_or_metro)
