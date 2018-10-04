from base64 import decodebytes
from os import remove
from PIL import Image
from pytesseract import *
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

all_number = []


def Namber(name):
    tessdata_dir_config = '--tessdata-dir "C:\Tesseract-OCR"'
    image = Image.open(name)
    number = image_to_string(image, config=tessdata_dir_config, lang='eng')
    return number


def write(img, name):
    while True:
        try:
            with open(name, "wb") as f:
                f.write(img)
            namber = Namber(name)
            remove("Avito.png")
            return namber
        except:
            continue


class NumberTelephone:
    def __init__(self, url):
        self.driver = webdriver.PhantomJS(executable_path=r'C:\Users\Dima\Downloads\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs')
        while True:
            try:
                self.driver.get(url)
                break
            except:
                continue
        name = self.getName()
        self.buttonClick()
        number = self.getNumber()
        data = "{} - {}".format(name, str(number))
        print(data)
        all_number.append(data)


    def getName(self):
        name = self.driver.find_element_by_xpath('//span[@class="title-info-title-text"]').text
        return name


    def buttonClick(self):
        while True:
            try:
                button = self.driver.find_element_by_xpath(
                    '//a[@class="button item-phone-button js-item-phone-button button-origin button-origin-blue button-origin_full-width button-origin_large-extra item-phone-button_hide-phone item-phone-button_card js-item-phone-button_card"]')
                button.click()
                break
            except:
                continue


    def getImage(self):
        image = self.driver.find_element_by_xpath('//div[@class="item-phone-big-number js-item-phone-big-number"]/img').get_attribute('src').split(',')[1]
        return image


    def getNumber(self):
        number = None
        while number is None:
            try:
                image = self.getImage()
                img = decodebytes(bytearray(image, 'utf-8'))
                number = write(img, "Avito.png")
            except NoSuchElementException:
                continue
        self.driver.quit()
        return number