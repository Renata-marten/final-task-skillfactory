from .base_page import BasePage
from .locators import Locators

import time,os


class MainPage(BasePage):

    def __init__(self, driver, timeout='10'):
        super().__init__(driver, timeout)
        url = os.getenv("MAIN_URL") or "https://tmall.ru/"
        driver.get(url)

#создаем нужные элементы
        self.logo_gif = driver.find_element(*Locators.LOGO_GIF)
        time.sleep(3)


    def click_logo(self):
        self.driver.find_element_by_class_name(self.logo_gif).click()
        time.sleep(3) #ждем реакции