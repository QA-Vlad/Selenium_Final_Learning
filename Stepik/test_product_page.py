import pytest

from Stepik.pages.basket_page import BasketPage
from Stepik.pages.login_page import LoginPage
from Stepik.pages.product_page import PageObject


# Тест проверки офферов за гостя
@pytest.mark.need_review
@pytest.mark.parametrize('link', [f"https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{i}" for i in range(10)])
def test_guest_can_add_product_to_basket(browser, link):
    product_page = PageObject(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.alert_check_and_send_answer()
    # Помечаем только offer7 как ожидаемо падающий
    if "offer7" in link:
        pytest.xfail("Известная проблема с offer7")
    product_page.check_book_and_basket()

# Тест перехода в корзину со страницы товара и проверка её пустоты
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/ru/catalogue/applied-cryptography_200"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_not_be_product_in_basket()
    page.should_be_basket_empty_message()


# Проверял что после добавление товара в корзину не появляется сообщение об этом (отрицательное тестирование)
@pytest.mark.xfail(reason="Ожидаемо падающий негативный тест")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = PageObject(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.should_not_be_success_message()


# Проверяет что при открытии странице нет сообщения об успешное добавление товара в корзину
def test_guest_cant_see_success_message(browser):
    link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = PageObject(browser, link)
    product_page.open()
    product_page.should_not_be_success_message()


# Проверяет что после появление сообщение о добавление товара в корзину, это сообщение пропадает через несколько сек
# (негативное тестирование)
@pytest.mark.xfail(reason="Ожидаемо падающий негативный тест")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = PageObject(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.should_disappear_element()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = PageObject(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = PageObject(browser, link)
    page.open()
    page.go_to_login_page()


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    # Рега перед каждым тестом + проверка, что рега удалась
    def setup(self, browser):
        link = "https://selenium1py.pythonanywhere.com"
        product_page = LoginPage(browser, link)
        product_page.open()
        product_page.register_new_user()
        product_page.should_be_authorized_user()

    # Проверяет что при открытии странице юзером нет сообщения об успешное добавление товара в корзину
    def test_user_cant_see_success_message(self, browser):
        link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        product_page = PageObject(browser, link)
        product_page.open()
        product_page.should_not_be_success_message()

    # Тест проверки офферов за гостя
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "https://selenium1py.pythonanywhere.com/de/catalogue/coders-at-work_207/?promo=offer1"
        product_page = PageObject(browser, link)
        product_page.open()
        product_page.add_to_basket()
        product_page.alert_check_and_send_answer()
        product_page.check_book_and_basket()
