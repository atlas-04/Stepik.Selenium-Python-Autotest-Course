from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

# тут пробуем провернуть задание из section1_lesson6_step11 через unittest

class TestSelectors(unittest.TestCase):
    # тест 1
    def test_registration1(self):
        link1 = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link1)
        write_text = "Congratulations! You have successfully registered!"

        input_first_name = browser.find_element(By.CSS_SELECTOR, "div.first_block > .first_class > .first")
        input_first_name.send_keys("Ivan")
        input_last_name = browser.find_element(By.CSS_SELECTOR, "div.first_block > .second_class > .second")
        input_last_name.send_keys("Petrov")
        input_email = browser.find_element(By.CSS_SELECTOR, "div.first_block > .third_class > .third")
        input_email.send_keys("test@stopik.by")
        input_phone = browser.find_element(By.CSS_SELECTOR, "div.second_block > .first_class > .first")
        input_phone.send_keys("557830")
        input_adress = browser.find_element(By.CSS_SELECTOR, "div.second_block > .second_class > .second")
        input_adress.send_keys("Russia")
        button = browser.find_element(By.CLASS_NAME, "btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(2)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assertEqual, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(write_text, welcome_text, "текст не совпал")

    def test_registration2(self):
        link2 = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link2)
        write_text = "Congratulations! You have successfully registered!"

        input_first_name = browser.find_element(By.CSS_SELECTOR, "div.first_block > .first_class > .first")
        input_first_name.send_keys("Ivan")
        input_last_name = browser.find_element(By.CSS_SELECTOR, "div.first_block > .second_class > .second")
        input_last_name.send_keys("Petrov")
        input_email = browser.find_element(By.CSS_SELECTOR, "div.first_block > .third_class > .third")
        input_email.send_keys("test@stopik.by")
        input_phone = browser.find_element(By.CSS_SELECTOR, "div.second_block > .first_class > .first")
        input_phone.send_keys("557830")
        input_adress = browser.find_element(By.CSS_SELECTOR, "div.second_block > .second_class > .second")
        input_adress.send_keys("Russia")
        button = browser.find_element(By.CLASS_NAME, "btn")
        button.click()
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(2)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assertEqual проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(write_text, welcome_text, "текст не совпал")

        # закрываем браузер после всех манипуляций
        browser.quit()


if __name__ == "__main__":
    unittest.main()