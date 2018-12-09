# coding=utf-8
import random
from base64 import decodebytes
from PIL import Image
from pytesseract import *
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from urllib3.exceptions import ProtocolError, MaxRetryError

goods_details = []


def get_goods_details(url):

    driver = webdriver.PhantomJS(executable_path=r'PhantomJS\phantomjs')

    try:
        driver.get(url)
    except (ProtocolError, MaxRetryError):
        driver.quit()
        print('Error conecting:', url)
        return None

    name_goods = get_name_goods(driver)

    button_click(driver)

    coded_image = get_coded_image(driver)

    image_in_bytes = get_image_in_bytes(coded_image)

    driver.quit()

    name_image = "AvitoIMG/Avito{}.png".format(random.randint(0, 100000))

    create_image(image_in_bytes, name_image)

    open_image = Image.open(name_image)

    phone_number = get_phone_number(open_image)

    data = "{} - {}".format(name_goods, str(phone_number))
    print(data)

    goods_details.append(data)

    return goods_details


def get_name_goods(driver):
    """ Метод возвращает название товара. """
    name_goods = driver.find_element_by_xpath('//span[@class="title-info-title-text"]').text
    return name_goods


def button_click(driver):
    """ Метод кликает на кнопку для получения номера телефона. """
    while True:
        try:
            button = driver.find_element_by_xpath(
                '//a[@class="button item-phone-button js-item-phone-button button-origin button-origin-blue button-origin_full-width button-origin_large-extra item-phone-button_hide-phone item-phone-button_card js-item-phone-button_card"]')
            button.click()
            break
        except NoSuchElementException:
            continue


def get_coded_image(driver):
    while True:
        try:
            coded_image = driver.find_element_by_xpath('//div[@class="item-phone-big-number js-item-phone-big-number"]/img').get_attribute('src').split(',')[1]
            return coded_image
        except NoSuchElementException:
            continue


def get_image_in_bytes(coded_image):
    """ Метод возвращает изображение номера телефона в байтах. """
    image_in_bytes = decodebytes(bytearray(coded_image, 'utf-8'))
    return image_in_bytes


def create_image(image_in_bytes, name_image):
    """ Метод создаёт изображение. """
    with open(name_image, "wb") as f:
        f.write(image_in_bytes)


def get_phone_number(open_image):
    """ Метод возвращает номер телефона. """
    config = '--tessdata-dir "Tesseract-OCR"'
    phone_number = image_to_string(open_image, config=config, lang='eng')
    return phone_number
