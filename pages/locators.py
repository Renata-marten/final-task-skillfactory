from selenium.webdriver.common.by import By
# импортируем класс, содержащий определения разных типов поиска

# здесь сначала пишем локаторы элементов страниц, которые собираемся использовать в проверках

class Locators:
    LOGO_GIF = (By.CLASS_NAME, "site-gif")
    LOGO_ALI = (By.CLASS_NAME, "logo-link")
