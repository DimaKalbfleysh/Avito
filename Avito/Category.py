from bs4 import BeautifulSoup
from Avito.Request import Request
from Avito.categories import categories


def getListCategories(html):
    soup = BeautifulSoup(html, 'lxml')
    all_li = soup.find('nav', class_='category-map').find_all('li', class_='category-map-item')
    links = []
    for li in all_li:
        try:
            href = li.find('a').get('href').split("/")[2]
            links.append(href)
        except:
            continue
    return links


def getDictCategories(ip_list):
    dict_categories = {}

    links = getListCategories(Request('https://www.avito.ru/', ip_list).getHtml())
    '''Получаем список категорий'''

    for category in categories:
        dict_categories[category] = links[categories.index(category)]
        '''
        Добавляем в словарь категории. Ключём является название категории на русском,
        значение является название категории на английском
        '''

    print(dict_categories)
    return dict_categories

