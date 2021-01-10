from selenium import webdriver
import config
import time
# time для задержек времени, можно потом убрать их все

from pages.main_page import MainPage
# импортируем класс страницы

''' для каждой страницы пишем тесты, используя объекты и методы предварительно описанные в файле страницы '''

def test_click_gif(web_browser):
    """ Проверим переход по лого-гифке в хедере. """
    page = MainPage(web_browser)
    page.logo_gif.click()
    # проверим, произошел ли переход с главной страницы
    assert page.get_domain() == config.ali_domain, "error clicking gif in header"

    time.sleep(5)
    web_browser.back()
    # возвращаемся на предыдущую страницу

def test_click_logo_ali(web_browser):
    """ Проверим переход по лого алиэкспресса в верхней панели страницы """
    page = MainPage(web_browser)
    page.logo_ali.click()
    # проверим, произошел ли переход с главной страницы
    assert page.get_domain() == config.ali_domain, "error clicking gif in header"