from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

# ниже мат. функция для Х
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/explicit_wait2.html')  # открыть ссылку

    # говорим Selenium проверять не менее 12 секунд, и пока цена не будет равна 100
    book = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
    # после находим кнопку 'book' и жмакаем её
    book_button = browser.find_element(By.ID, 'book')
    book_button.click()

    # решаем капчу
    x_element = browser.find_element(By.ID, 'input_value')  # находим значение x
    x = x_element.text  # присваиваемм значение переменной x
    y = calc(x)  # считаем математическую функцию для x

    # вводим мат. Х в ответ
    input_answer = browser.find_element(By.ID, 'answer') #находим поле ввода мат. значения
    input_answer.send_keys(y) #вводим туда мат. x

    # засабмитили болевым
    button = browser.find_element(By.ID, 'solve')
    button.click()

finally:
    # успеваем скопировать код за 15 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
    )
button.click()
message = browser.find_element_by_id("verify_message")

assert "successful" in message.text