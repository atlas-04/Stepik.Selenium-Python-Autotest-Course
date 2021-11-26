from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

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
    time.sleep(5)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # успеваем скопировать код за 15 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла