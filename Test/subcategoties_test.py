from Avito.category import get_dict_categories
from Avito.proxies import get_proxy
from Avito.subcategories import get_subcategories

list_ip = get_proxy()
categories = get_dict_categories(list_ip)
category = categories["Мотоциклы и мототехника"]

while True:
    subcategories = get_subcategories(category, list_ip)
