# Avito
Парсер Авито

Скрипт парсит, с сайта https://avito.ru, данные:
 Название товара,
 Цена товара,
 Url товара,
 Номер телефона продавца. 
И записывает их в Excel таблицу.
В файле __main__:

city = cities["Ижевск"] # Замените "Ижевск" на нужный Вам город

category = categories["Велосипеды"] # Замените "Велосипеды" на нужную Вам категорию

links_to_product_pages = linksToProductPages(city, category, subcategories, district['Октябрьский'], proxy_list, "district") # Замените "Октябрьский" на нужный Вам район, если нужен весь город, то передайте district



