import threading
from Avito.Number import NumberTelephone, all_number


def getNumberTelephone(urls, n):
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
        r = threading.Thread(target=Threading, args=(lists[lists.index(list)],))
        r.start()


def Threading(urls):
    for url in urls:
        NumberTelephone(url)
        print(len(all_number))
