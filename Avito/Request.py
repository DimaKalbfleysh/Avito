# coding=utf-8
from requests import get
from requests.exceptions import ProxyError, ReadTimeout, SSLError, ConnectionError


class Request:
    def __init__(self, url, list_ip):
        self.url = url
        self.list_ip = list_ip
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}

    def getHtml(self, returned=None):
        for ip in self.list_ip:
            try:
                html = self.response(ip)
                if html is not None:
                    if returned == "url": return self.url
                    return html
            except (ProxyError, ConnectionError, ReadTimeout, SSLError):
                self.list_ip.pop(self.list_ip.index(ip))
                continue

    def response(self, ip):
        r = get(self.url, proxies={"https": ip}, headers=self.headers, timeout=7)
        if len(r.text) > 80000:
            return r.text

    def forMetro(self):
        for ip in self.list_ip:
            try:
                r = get(self.url, proxies={"https": ip}, headers=self.headers, timeout=5)
                return r.text
            except (ProxyError, ConnectionError, ReadTimeout, SSLError):
                self.list_ip.pop(self.list_ip.index(ip))
                continue
