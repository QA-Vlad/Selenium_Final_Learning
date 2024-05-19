from Stepik.pages.base_page import BasePage
from Stepik.pages.locators import BasketPageLocators


class BasketPage(BasePage):
    # Метод проверки того что в корзине нет товаров
    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_NOT_EMPTY), \
            "Корзина не пуста, хотя должна быть пустой"

    # Метод проверки того что есть надпись о том что корзина пуста
    def should_be_basket_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), \
            "Нет нужной надписи о том что корзина пуста"

