from .base_page import BasePage
# импортируем базовый класс страницы
from .locators import Locators
# импортируем класс локаторов

import time,os
# модуль time для задержек, можно потом удалить их
# модуль os чтобы использовать метод getenv чтобы получить доступ к переменным среды.

''' для каждой страницы пишем методы к локаторам '''

class MainPage(BasePage):

    def __init__(self, driver, timeout='10'):
        super().__init__(driver, timeout)
        url = os.getenv("MAIN_URL") or "https://tmall.ru/"
        driver.get(url)

        #создаем нужные элементы
        self.logo_gif = driver.find_element(*Locators.LOGO_GIF)
        time.sleep(3)
        self.logo_ali = driver.find_element(*Locators.LOGO_ALI)







