from urllib.parse import urlparse
# из библиотеки urllib будет использован метод get_relative_link

class BasePage(object):
    # конструктор класса - специальный метод с ключевым словом __init__
    # Нам нужны объект веб-драйвера, адрес страницы и время ожидания элементов
    def __init__(self, driver, url, timeout=10):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)

    # дальше будут базовые действия для любой страницы

    # def get(self, url):
    #     self.driver.get(url)
    #     self.wait_page_loaded()

    # метод для определения, на какой странице мы находимся
    def get_current_link(self):
        return self.driver.current_url

    def get_relative_link(self):
        url = urlparse(self.driver.current_url)
        return url.path

    def get_domain(self):
        url = urlparse(self.driver.current_url)
        return url.netloc

    # def wait_page_loaded(self, timeout=60, check_js_comlete=True,
    #                      check_page_changes=False, check_images=False,
    #                      wait_for_element=None, wait_for_xpath_to_disappear='', sleep_time=2):
