import math
import pyperclip
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():
    # Инициализация браузера и неявных ожиданий
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    # Метод открытие страницы
    def open(self):
        self.browser.get(self.url)

    # Метод проверки наличия элемента на странице
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    # Метод проверки отсутствия элемента на странице
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    #  Метод проверки того, что какой-либо элемент (например, всплывающее окно,
    #  модальное окно или спиннер загрузки) исчезает со страницы в течение заданного времени ожидания.
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    # Получение кода от викторины (выводится в лог и копируется в буфер обмена)
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert_text = alert_text.split(': ')[-1]
            pyperclip.copy(alert_text)
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

