import time
from Avito.Proxies import getProxy
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

proxy_list = []
def getIP():
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    driver = webdriver.Firefox(executable_path=r'C:\Users\Dima\Downloads\geckodriver', options=options)
    driver.get("https://hidemyna.me/ru/proxy-list/")
    time.sleep(15)
    tbody = driver.find_element_by_xpath('//tbody').text.split("\n")
    for td in tbody:
        if tbody.index(td)%4==0:
            proxy = td.split(" ")
            ip = proxy[0]
            port = proxy[1]
            proxy = "{}:{}".format(ip, port)
            proxy_list.append(proxy)
    print(proxy_list)
    driver.quit()
    return proxy_list


def Proxy():
    ip_list = []
    px = []
    proxy_list = getProxy()
    for proxy in proxy_list:
        try:
            for x in range(2):
                r = requests.get("http://pubproxy.com/api/proxy?limit=20&format=txt&type=https", proxies={"http": proxy})
                html = r.text
                soup = BeautifulSoup(html, "lxml")
                px = px + soup.text.split("\n")
            break
        except:
            continue
    for ip in px:
        ip_list.append(ip)
    print(ip_list)
    return ip_list
