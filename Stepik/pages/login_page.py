from selenium.webdriver.common.by import By

from Stepik.pages.base_page import BasePage
from Stepik.pages.locators import LoginPageLocators

link = "https://selenium1py.pythonanywhere.com/ru/accounts/login"


class LoginPage(BasePage):
    # Метод для вызова 3 методов ниже
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    # Методы для проверки соответствия ссылки логина в браузерной строке
    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "URL не соответствует"

    # Метод для проверки наличия формы логина
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Форма логина отсутствует"

    # Метод для проверки наличия формы регистрации
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Форма регистрации отсутствует"

    #  Находит ссылку перехода на страницу входа, кликает на нее, переключается на всплывающее окно и принимает его.
    def go_to_login_page(self):
        link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        link.click()
        alert = self.browser.switch_to.alert
        alert.accept()
        