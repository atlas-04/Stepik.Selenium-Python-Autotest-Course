from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"

# давно пора сказать - ниже мат. функция для Х
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # находим магическую кнопку и жмём
    magic_button = browser.find_element(By.CLASS_NAME, 'btn-primary')
    magic_button.click()
    time.sleep(3)

    # работаем с аллертами
    magic_confirm = browser.switch_to.alert  # нашли
    magic_confirm.accept()  # нажали ОК

    # решаем капчу
    x_element = browser.find_element(By.ID, "input_value")  # находим значение x
    x = x_element.text  # присваиваемм значение переменной x
    y = calc(x)  # считаем математическую функцию для x

    # вводим мат. Х в ответ
    input_answer = browser.find_element(By.ID, "answer") #находим поле ввода мат. значения
    input_answer.send_keys(y) #вводим туда мат. x

    # засабмитили болевым
    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()

finally:
    # успеваем скопировать код за 15 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()