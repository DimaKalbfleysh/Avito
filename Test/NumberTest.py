# coding=utf-8
from Avito.Goods import getGoods
from Avito.NumberTelephone import getNumberTelephone
from Avito.Proxies import getProxy

proxy_list = getProxy()
goods = getGoods(["https://avito.ru/izhevsk/velosipedy/zapchasti_i_aksessuary?p=4&district=164",
                  "https://avito.ru/izhevsk/velosipedy/zapchasti_i_aksessuary?p=3&district=164",
                  "https://avito.ru/izhevsk/velosipedy/zapchasti_i_aksessuary?p=2&district=164",
                  "https://avito.ru/izhevsk/velosipedy/zapchasti_i_aksessuary?p=1&district=164"], proxy_list)

# Колличество потоков
n = 5

numbers = getNumberTelephone(goods, n)
