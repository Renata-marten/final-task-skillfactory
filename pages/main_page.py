from .base_page import BasePage
# импортируем базовый класс страницы
from .locators import Locators
# импортируем класс локаторов

import time,os
# модуль time для задержек, можно потом удалить их
# модуль os чтобы использовать метод getenv чтобы получить доступ к переменным среды.

''' для каждой страницы описыаем элементы, используя локаторы из файла locators '''

class MainPage(BasePage):

    def __init__(self, driver, timeout='10'):
        super().__init__(driver, timeout)
        url = os.getenv("MAIN_URL") or "https://tmall.ru/"
        driver.get(url)

        #создаем нужные элементы страницы
        #лого алиэкспресс в верхней панели
        self.logo_gif = driver.find_element(*Locators.LOGO_GIF)
        #лого-гифка справа от лого т-молла
        self.logo_ali = driver.find_element(*Locators.LOGO_ALI)
        #поле поиска
        self.search_field = driver.find_element(*Locators.SEARCH_FIELD)
        #кнопка поиска
        self.search_button = driver.find_element(*Locators.SEARCH_BUTTON)
        #карточка товара в каталоге
        self.product_items = driver.find_elements(*Locators.PRODUCT_ITEMS)
        self.count_items = len(driver.find_elements(*Locators.PRODUCT_ITEMS))








