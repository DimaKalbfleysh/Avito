# coding=utf-8
import requests
from bs4 import BeautifulSoup

proxy_list = []


def get_html(url):
    r = requests.get(url)
    return r.text


def list_iP(html):
    soup = BeautifulSoup(html, "lxml")
    trs = soup.find("tbody").find_all("tr")
    for tr in trs:
        ip = tr.find_all("td")[0].text
        port = tr.find_all("td")[1].text
        proxy = "{}:{}".format(ip, port)
        proxy_list.append(proxy)
    return proxy_list


def get_proxy():
    """ Функция возвращает список https прокси. """
    url = "https://www.sslproxies.org/"
    proxy_list = list_iP(get_html(url))
    return proxy_list




