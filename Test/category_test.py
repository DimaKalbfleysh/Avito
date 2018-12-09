from Avito.category import get_dict_categories
from Avito.proxies import get_proxy

list_ip = get_proxy()
while True:
    print(get_dict_categories(list_ip))
