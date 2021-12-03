import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# link = 'https://p-on.ru/login'
link = 'http://test01.p-on.test/login'
last_name = 'Регистрации_Автоматический'
first_name = 'Тест'
batya_name = 'Тестович'
phone = '8953330555'
email = 'r.arakcheev13@alarmtrade.ru'
password = 'Qwerty45'

@pytest.fixture(scope='class')
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)  # до 10 секунд ожидаем появление кнопки "Регистрация"
    yield browser
    #time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

class Test_Registration():

    def test_one(self, browser):
        browser.get(link)

        # нашли кнопку регистрации и нажали
        register_button = browser.find_element(By.ID, 'register_button')
        register_button.click()

        # открыли правила предоставления сервиса
        reg_rules = browser.find_element(By.CLASS_NAME, 'reg-rules')
        reg_rules.click()

        # проверяем скролл в соглашении
        scroll_pane = browser.find_element(By.CLASS_NAME, 'scroll-pane')
        scroll_pane.click()
        rr_window = browser.find_element(By.CLASS_NAME, 'jspPane')
        scroll_pane.send_keys(Keys.END) # прожали END
        rr_window_down = int((rr_window.value_of_css_property('top'))[:-2])  # пробуем получить в переменную данные смещения скроллбара
        assert rr_window_down < 0, 'скроллбар не сместился вниз' # проверяем сместился ли скроллбар вниз

        scroll_pane.send_keys(Keys.HOME)
        rr_window_up = int((rr_window.value_of_css_property('top'))[:-2])
        assert rr_window_up == 0, 'скроллбар не сместился вверх'

        # закрыли правила предоставления сервиса
        reg_rules_close = browser.find_element(By.CLASS_NAME, 'bottom')
        reg_rules_close.click()

        # нашли кнопку "я согласен" и нажали
        reg_rules_yes = browser.find_element(By.CSS_SELECTOR, '.slide1 > div > .next')
        reg_rules_yes.click()
        time.sleep(2) #эксперимент с timeout exeption

        # нашли кнопку (через Explicit Waits) "частное лицо" и нажали
        reg_rules_man = browser.find_element(By.CSS_SELECTOR, '.slide2 > div > .next') # эксперимент с timeout exeption
        #reg_rules_man = WebDriverWait(browser, 5).until(EC.element_to_be_clickable ((By.CSS_SELECTOR, '.slide2 > div > .next')))
        reg_rules_man.click()

        # Заполняем ФИО, телефон, жмём "далее"
        # Фамилия
        input_last_name = browser.find_element(By.CSS_SELECTOR, '.slide3 > .form > [name="name_f"]')
        input_last_name.clear()
        input_last_name.send_keys(last_name)
        # Имя
        input_first_name = browser.find_element(By.CSS_SELECTOR, '.slide3 > .form > [name="name_i"]')
        input_first_name.clear()
        input_first_name.send_keys(first_name)
        # Отчество
        input_batya_name = browser.find_element(By.CSS_SELECTOR, '.slide3 > .form > [name="name_o"]')
        input_batya_name.clear()
        input_batya_name.send_keys(batya_name)
        # Телефон
        input_phone = browser.find_element(By.CSS_SELECTOR, '.slide3 > .form > [name="phone"]')
        input_phone.clear()
        input_phone.send_keys(phone)
        # Жмём "Далее"
        fio_phone_yes = browser.find_element(By.CSS_SELECTOR, '.slide3 > div > .next')
        fio_phone_yes.click()

        # Заполняем email, pass, жмём "далее"
        # Email
        input_email = browser.find_element(By.CSS_SELECTOR, '.slide4 > .form > [name="email"]')
        input_email.clear()
        input_email.send_keys(email)
        # Пароль
        input_password = browser.find_element(By.ID, 'password-person')
        input_password.clear()
        input_password.send_keys(password)

        # нажимаем "показать текст пароля"
        show_pass = browser.find_element(By.ID, 'pass-show-text')
        show_pass.click()
        # проверяем "показать текст пароля"
        input_repeat_password = browser.find_element(By.ID, 'password2-person')
        show_pass_text = input_repeat_password.get_attribute("type")
        # print(show_pass_text)
        assert show_pass_text == 'text', 'должен быть type="text"'
        # нажимаем "скрыть текст пароля"
        show_pass.click()
        # проверяем "скрыть текст пароля"
        show_pass_pass = input_repeat_password.get_attribute("type")
        # print(show_pass_pass)
        assert show_pass_pass == 'password', 'должен быть type="password"'

        # повторяем пароль
        input_repeat_password.clear()
        input_repeat_password.send_keys(password)
        # Жмём "Далее"
        email_pass_yes = browser.find_element(By.ID, 'reg-done-btn-person')
        email_pass_yes.click()

        # находим email успешной регистрации и проверяем его
        reg_usermail = browser.find_element(By.CSS_SELECTOR, '.slide5 span')
        reg_email = reg_usermail.get_attribute('innerHTML')
        assert reg_email == email
        # time.sleep(10)

        # находим и нажимаем "закрыть" в окнеу успешной регистрации
        finish_button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.slide5 .finish')))
        finish_button.click()
