# coding=utf-8
import requests
from bs4 import BeautifulSoup

proxy_list = []


def getHtml(url):
    r = requests.get(url)
    return r.text


def listIP(html):
    soup = BeautifulSoup(html, "lxml")
    trs = soup.find("tbody").find_all("tr")
    for tr in trs:
        ip = tr.find_all("td")[0].text
        port = tr.find_all("td")[1].text
        proxy = "{}:{}".format(ip, port)
        proxy_list.append(proxy)
    return proxy_list


def getProxy():
    """ Функция возвращает список https прокси. """
    url = "https://www.sslproxies.org/"
    proxy_list = listIP(getHtml(url))
    return proxy_list




