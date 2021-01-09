import time
from selenium import webdriver
from pages.main_page import MainPage


def test_main_page(web_browser):
    """ Проверим переход по лого в хедере. """
    url = "https://tmall.ru/"
    page = MainPage(web_browser, url)
    page.logo_gif.click()



    time.sleep(15)