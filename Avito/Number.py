# coding=utf-8
from base64 import decodebytes
from PIL import Image
from pytesseract import *
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

all_number = []


class NumberTelephone:
    def __init__(self, url, index1, index2):
        self.driver = webdriver.PhantomJS(executable_path=r'C:\Users\Dima\Downloads\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs')
        self.url = url
        self.name = "AvitoIMG/Avito{}{}.png".format(index1, index2)

    def main(self):
        while True:
            try:
                self.driver.get(self.url)
                break
            except:
                continue
        name = self.getName()
        self.buttonClick()
        image = self.getImage()
        self.write(image)
        number = self.getNamber()
        data = "{} - {}".format(name, str(number))
        print(data)
        all_number.append(data)

    def getName(self):
        """ Метод возвращает название товара. """
        name = self.driver.find_element_by_xpath('//span[@class="title-info-title-text"]').text
        return name

    def buttonClick(self):
        """ Метод кликает на кнопку для получения номера телефона. """
        while True:
            try:
                button = self.driver.find_element_by_xpath(
                    '//a[@class="button item-phone-button js-item-phone-button button-origin button-origin-blue button-origin_full-width button-origin_large-extra item-phone-button_hide-phone item-phone-button_card js-item-phone-button_card"]')
                button.click()
                break
            except:
                continue

    def getImage(self):
        """ Метод возвращает изображение номера телефона в байтах. """
        while True:
            try:
                image = self.driver.find_element_by_xpath(
                    '//div[@class="item-phone-big-number js-item-phone-big-number"]/img').get_attribute('src').split(
                    ',')[1]
                img = decodebytes(bytearray(image, 'utf-8'))
                self.driver.quit()
                return img
            except NoSuchElementException:
                continue

    def write(self, img):
        with open(self.name, "wb") as f:
            f.write(img)

    def getNamber(self):
        """ Метод возвращает номер телефона. """
        tessdata_dir_config = '--tessdata-dir "C:\Tesseract-OCR"'
        image = Image.open(self.name)
        number = image_to_string(image, config=tessdata_dir_config, lang='eng')
        return number
