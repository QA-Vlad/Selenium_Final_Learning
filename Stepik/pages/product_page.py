import re
from selenium.common import TimeoutException
from Stepik.pages.base_page import BasePage
from Stepik.pages.locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageObject(BasePage):

    # Метод для проверки наличия кнопки корзины и клика на неё
    def add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), "Кнопка корзины отсутствует"
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()

    # Проверка алёрта
    def alert_check(self):
        try:
            alert = WebDriverWait(self.browser, 10).until(EC.alert_is_present())
            alert_text = alert.text
            # Проверка текста алерта
            expected_text = "log10(abs(12*sin(x)))"
            assert expected_text in alert_text, f"Ожидаемый текст '{expected_text}' отсутствует в алерте"

            print(f"Текст алерта: {alert_text}")

        except TimeoutException:
            print("Алерт не появился")

    # Решаем викторину и получаем код
    def alert_send_answer(self):
        self.solve_quiz_and_get_code()

    # Объединяю в один вызов несколько методов
    def alert_check_and_send_answer(self):
        self.alert_check()
        self.alert_send_answer()

    def check_book_add_to_basket(self):
        # Проверка сообщения о добавлении товара в корзину
        assert self.is_element_present(*ProductPageLocators.BOOK_ADD_GOOD), "Сообщение о добавлении товара в корзину отсутствует"

    def check_book_name_and_book_name_in_basket(self):
        # Проверка названия книги на странице товара
        assert self.is_element_present(*ProductPageLocators.BOOK_NAME), "Название книги отсутствует на странице"
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        print(f"Название книги на странице: {book_name}")

        # Проверка названия книги в корзине
        book_name_in_basket = self.browser.find_element(*ProductPageLocators.BOOK_ADD_GOOD).text
        print(f"Название книги в корзине: {book_name_in_basket}")
        assert book_name == book_name_in_basket, "Название книги на странице товара и название книги в корзине не совпадают"

    def check_card_add_message(self):
        assert self.is_element_present(*ProductPageLocators.CARD_VALUE_MESSAGE), 'Сообщение о добавление товара в корзину отсутствует'
        card_value_message = self.browser.find_element(*ProductPageLocators.CARD_VALUE_MESSAGE).text

    def check_basket_price_equals_book_price(self):
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        basket_price = ''.join(re.findall(r'\d+', basket_price))   # Достаю только цифры из строки для дальнейшего сравнения

        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        book_price = ''.join(re.findall(r'\d+', book_price))   # Достаю только цифры из строки для дальнейшего сравнения

        assert basket_price == book_price, "Цена книги в корзине и цена книги на странице товара не совпадают"

    # Объединяю в один вызов несколько методов
    def check_book_and_basket(self):
        self.check_book_add_to_basket()
        self.check_book_name_and_book_name_in_basket()
        self.check_card_add_message()
        self.check_basket_price_equals_book_price()

    # Проверка того что элемент не появился за определённо время (отрицательное тестирование)
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.BOOK_ADD_GOOD), \
            "Появилось сообщение об успехи, но не должно было"

    # Проверка того что элемент пропал за определённо время (отрицательное тестирование)
    def should_disappear_element(self):
        assert self.is_disappeared(*ProductPageLocators.BOOK_ADD_GOOD), "Сообщение об успехи не пропало"

