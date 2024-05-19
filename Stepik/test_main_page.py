import pytest
from Stepik.pages.main_page import MainPage
from Stepik.pages.login_page import LoginPage
from Stepik.pages.basket_page import BasketPage


@pytest.mark.login_guest
class TestLoginFromMainPage():
    # Проверяем что есть линк логина на странице
    def test_guest_should_see_login_link(self, browser):
        link = "https://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open() # открываем страницу
        page.should_be_login_link()

    def test_guest_can_go_to_login_page(self, browser):
        link = "https://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()


def test_guest_can_see_login_form(browser):   #Проверяем наличие формы логина
    link = "https://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()  # открываем страницу
    page.should_be_login_form()


def test_guest_can_see_register_form(browser):   #Проверяем наличие формы регистрации
    link = "https://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()  # открываем страницу
    page.should_be_register_form()


# Проверяем что есть линк логина на странице
def test_guest_should_see_login_link(browser):
    link = "https://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()  # переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_url()  # теперь проверяем URL страницы логина


# Тест перехода в корзину с главной странице и проверка её пустоты
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "https://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_not_be_product_in_basket()
    page.should_be_basket_empty_message()


# Тест перехода в корзину со страницы товара и проверка её пустоты
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/ru/catalogue/applied-cryptography_200"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_not_be_product_in_basket()
    page.should_be_basket_empty_message()
