# coding=utf-8
import threading
from os import mkdir
from shutil import rmtree
from Avito.Number import NumberTelephone, all_number


def getNumberTelephone(urls, n):
    """ Функция возвращает список номеров телефона продавцов. """
    try:
        rmtree("AvitoIMG")
        mkdir("AvitoIMG")
    except:
        mkdir("AvitoIMG")
    lists = [[] for q in range(n)]
    q = 0
    while len(urls) > 0:
        try:
            for list in lists:
                list.append(urls[q])
                urls.pop(urls.index(urls[q]))
        except:
            break

    for list in lists:
        r = threading.Thread(target=Threading, args=(lists[lists.index(list)], lists.index(list)))
        r.start()


def Threading(urls, index):
    for url in urls:
        number = NumberTelephone(url, urls.index(url), index)
        number.main()
        print(len(all_number))
    print(all_number)
    return all_number
