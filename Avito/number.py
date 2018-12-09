# coding=utf-8
import random
from base64 import decodebytes
from PIL import Image
from pytesseract import *
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from urllib3.exceptions import ProtocolError, MaxRetryError

all_number = []


def main(url):
    driver = webdriver.PhantomJS(executable_path=r'PhantomJS\phantomjs')
    name_image = "AvitoIMG/Avito{}.png".format(random.randint(0, 100000))
    try:
        driver.get(url)
    except (ProtocolError, MaxRetryError):
        driver.quit()
        print('Error conecting:', url)
        return None
    name_good = get_name_good(driver)
    button_click(driver)
    image = get_image(driver)
    image = decoding(image)
    driver.quit()
    write(image, name_image)
    image = Image.open(name_image)
    config = '--tessdata-dir "Tesseract-OCR"'
    number = get_namber(image, config)
    data = "{} - {}".format(name_good, str(number))
    print(data)
    all_number.append(data)
    return all_number


def get_name_good(driver):
    """ Метод возвращает название товара. """
    name = driver.find_element_by_xpath('//span[@class="title-info-title-text"]').text
    return name


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


def get_image(driver):
    """ Метод возвращает изображение номера телефона в байтах. """
    while True:
        try:
            image = driver.find_element_by_xpath('//div[@class="item-phone-big-number js-item-phone-big-number"]/img').get_attribute('src').split(',')[1]
            return image
        except NoSuchElementException:
            continue


def decoding(image):
    img = decodebytes(bytearray(image, 'utf-8'))
    return img


def write(img, name):
    with open(name, "wb") as f:
        f.write(img)


def get_namber(image, config):
    """ Метод возвращает номер телефона. """
    number = image_to_string(image, config=config, lang='eng')
    return number
