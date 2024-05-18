import time

from Stepik.pages.product_page import PageObject


def test_guest_can_add_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = PageObject(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.alert_check_and_send_answer()
    product_page.check_book_and_basket()
    time.sleep(1)
