import requests
from bs4 import BeautifulSoup
proxy_list = []


def getHtml(url):
    r = requests.get(url)
    return r.text


def listIP(html):
    soup = BeautifulSoup(html, "lxml")
    tds = soup.find("tbody").find_all("tr")
    for td in tds:
        ip = td.find_all("td")[0].text
        port = td.find_all("td")[1].text
        proxy = "{}:{}".format(ip, port)
        proxy_list.append(proxy)
    print(len(proxy_list))
    return proxy_list


def getProxy():
    url = "https://www.sslproxies.org/"
    proxy_list = listIP(getHtml(url))
    return proxy_list




