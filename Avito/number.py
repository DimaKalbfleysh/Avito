# coding=utf-8
from base64 import decodebytes
from PIL import Image
from pytesseract import *
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from urllib3.exceptions import ProtocolError

all_number = []


def main(url, index1, index2):
    driver = webdriver.PhantomJS(executable_path=r'PhantomJS\phantomjs')
    name_image = "AvitoIMG/Avito{}{}.png".format(index1, index2)
    while True:
        try:
            driver.get(url)
            break
        except ProtocolError:
            continue
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


# class NumberTelephone:
#     def __init__(self, url, index1, index2):
#         self.driver = webdriver.PhantomJS(executable_path=r'PhantomJS\phantomjs')
#         self.url = url
#         self.name = "AvitoIMG/Avito{}{}.png".format(index1, index2)
#         self.tessdata_dir_config = '--tessdata-dir "C:\Tesseract-OCR"'
#
#     def main(self):
#         while True:
#             try:
#                 self.driver.get(self.url)
#                 break
#             except:
#                 continue
#         name = self.get_name()
#         self.button_click()
#         image = self.get_image()
#         self.write(image)
#         number = self.get_namber()
#         data = "{} - {}".format(name, str(number))
#         print(data)
#         all_number.append(data)
#
#     def get_name(self):
#         """ Метод возвращает название товара. """
#         name = self.driver.find_element_by_xpath('//span[@class="title-info-title-text"]').text
#         return name
#
#     def button_click(self):
#         """ Метод кликает на кнопку для получения номера телефона. """
#         while True:
#             try:
#                 button = self.driver.find_element_by_xpath(
#                     '//a[@class="button item-phone-button js-item-phone-button button-origin button-origin-blue button-origin_full-width button-origin_large-extra item-phone-button_hide-phone item-phone-button_card js-item-phone-button_card"]')
#                 button.click()
#                 break
#             except:
#                 continue
#
#     def get_image(self):
#         """ Метод возвращает изображение номера телефона в байтах. """
#         while True:
#             try:
#                 image = self.driver.find_element_by_xpath('//div[@class="item-phone-big-number js-item-phone-big-number"]/img').get_attribute('src').split(',')[1]
#                 img = decodebytes(bytearray(image, 'utf-8'))
#                 self.driver.quit()
#                 return img
#             except NoSuchElementException:
#                 continue
#
#     def write(self, img):
#         with open(self.name, "wb") as f:
#             f.write(img)
#
#     def get_namber(self):
#         """ Метод возвращает номер телефона. """
#         image = Image.open(self.name)
#         number = image_to_string(image, config=self.tessdata_dir_config, lang='eng')
#         return number
