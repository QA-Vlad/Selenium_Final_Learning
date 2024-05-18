import time

import pytest

from Stepik.pages.product_page import PageObject


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
