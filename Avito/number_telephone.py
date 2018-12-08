# coding=utf-8
import threading
from os import mkdir
from shutil import rmtree
from Avito.number import main, all_number


def get_number_telephone(urls, n):
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
        r = threading.Thread(target=thread, args=(lists[lists.index(list)], lists.index(list)))
        r.start()


def thread(urls, index):
    for url in urls:
        number = main(url, urls.index(url), index)
        print(len(all_number))
    print(all_number)
    return all_number
