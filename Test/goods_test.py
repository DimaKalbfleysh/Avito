from Avito.goods import get_goods
from Avito.proxies import get_proxy

proxy = get_proxy()
urls = ['https://avito.ru/izhevsk/velosipedy/gornye?p=1&district=164',
        'https://avito.ru/izhevsk/velosipedy/gornye?p=2&district=164']
goods = get_goods(urls, proxy)
for good in goods:
    print(good)
