# coding=utf-8
from Avito.goods import get_goods
from Avito.number_telephone import get_number_telephone
from Avito.proxies import get_proxy

proxy_list = get_proxy()
goods = get_goods(["https://avito.ru/izhevsk/velosipedy/zapchasti_i_aksessuary?p=3&district=164",], proxy_list)

# Колличество потоков
n = 5

numbers = get_number_telephone(goods, n)
