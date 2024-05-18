from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators():
    BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")  # Кнопка добавления в корзину
    BOOK_NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main > h1")  # Имя книги на странице
    BOOK_PRICE = (By.CSS_SELECTOR, "h1 + p.price_color")   # Цена книги на странице
    BOOK_ADD_GOOD = (By.CSS_SELECTOR, "div.alert.alert-success:first-of-type .alertinner > strong")  # Текст уведомления о добавлении книги в корзину
    CARD_VALUE_MESSAGE = (By.CLASS_NAME, "alert-info")  # Сообщение о добавление товара в корзину вместе с появившейся стоимостью
    BASKET_TOTAL = (By.CSS_SELECTOR, ".basket-mini.pull-right")  # Итоговая цена товаров в корзине



