import time

import pytest

from Stepik.pages.product_page import PageObject

#
# @pytest.mark.parametrize('link', [f"https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{i}" for i in range(10)])
# def test_guest_can_add_product_to_basket(browser, link):
#     product_page = PageObject(browser, link)
#     product_page.open()
#     product_page.add_to_basket()
#     product_page.alert_check_and_send_answer()
#     # Помечаем только offer7 как ожидаемо падающий
#     if "offer7" in link:
#         pytest.xfail("Известная проблема с offer7")
#     product_page.check_book_and_basket()


link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


# Проверял что после добавление товара в корзину не появляется сообщение об этом (отрицательное тестирование)
@pytest.mark.xfail(reason="Ожидаемо падающий негативный тест")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_page = PageObject(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.should_not_be_success_message()


# Проверяет что при открытии странице нет сообщения об успешное добавление товара в корзину
def test_guest_cant_see_success_message(browser):
    product_page = PageObject(browser, link)
    product_page.open()
    product_page.should_not_be_success_message()


# Проверяет что после появление сообщение о добавление товара в корзину, это сообщение пропадает через несколько сек
# (негативное тестирование)
@pytest.mark.xfail(reason="Ожидаемо падающий негативный тест")
def test_message_disappeared_after_adding_product_to_basket(browser):
    product_page = PageObject(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.should_disappear_element()
