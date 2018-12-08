# coding=utf-8
from Avito.Goods import get_goods
from Avito.NumberTelephone import get_number_telephone
from Avito.Proxies import get_proxy

proxy_list = get_proxy()
goods = get_goods(["https://avito.ru/izhevsk/velosipedy/zapchasti_i_aksessuary?p=4&district=164",
                  "https://avito.ru/izhevsk/velosipedy/zapchasti_i_aksessuary?p=3&district=164",
                  "https://avito.ru/izhevsk/velosipedy/zapchasti_i_aksessuary?p=2&district=164",
                  "https://avito.ru/izhevsk/velosipedy/zapchasti_i_aksessuary?p=1&district=164"], proxy_list)

# Колличество потоков
n = 5

numbers = get_number_telephone(goods, n)
