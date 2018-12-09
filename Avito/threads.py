# coding=utf-8
from threading import Thread
from os import mkdir
from shutil import rmtree
from Avito.goods_details import get_goods_details, goods_details
import numpy


def start_threads(urls, number_of_threads):
    """ Функция возвращает список номеров телефона продавцов. """
    try:
        rmtree("AvitoIMG")
        mkdir("AvitoIMG")
    except FileNotFoundError:
        mkdir("AvitoIMG")

    lists_urls = list(numpy.array_split(urls, number_of_threads))
    for list_urls in lists_urls:
        thd = Thread(target=thread, args=(list_urls,))
        thd.start()


def thread(list_urls):
    for url in list_urls:
        get_goods_details(url)
        print(len(goods_details))
