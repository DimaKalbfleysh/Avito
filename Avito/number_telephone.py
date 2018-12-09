# coding=utf-8
from threading import Thread
from os import mkdir
from shutil import rmtree
from Avito.number import main, all_number
import numpy


def get_number_telephone(urls, number_of_threads):
    """ Функция возвращает список номеров телефона продавцов. """
    try:
        rmtree("AvitoIMG")
        mkdir("AvitoIMG")
    except FileNotFoundError:
        mkdir("AvitoIMG")

    lists_urls = list(numpy.array_split(urls, number_of_threads))
    for list_urls in lists_urls:
        r = Thread(target=thread, args=(list_urls,))
        r.start()


def thread(list_urls):
    for url in list_urls:
        number = main(url)
        print(len(all_number))
