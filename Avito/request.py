# coding=utf-8
from requests import get
from requests.exceptions import ProxyError, ReadTimeout, SSLError, ConnectionError


def get_html(url, list_ip):
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
    for ip in list_ip:
        try:
            html = response(url, ip, headers)
            if html is not None: return html
        except (ProxyError, ConnectionError, ReadTimeout, SSLError):
            list_ip.pop(list_ip.index(ip))
            continue


def response(url, ip, headers):
    r = get(url, proxies={"https": ip}, headers=headers, timeout=7)
    if len(r.text) > 80000:
        return r.text


def for_metro(url, list_ip, headers):
    for ip in list_ip:
        try:
            r = get(url, proxies={"https": ip}, headers=headers, timeout=5)
            return r.text
        except (ProxyError, ConnectionError, ReadTimeout, SSLError):
            list_ip.pop(list_ip.index(ip))
            continue
