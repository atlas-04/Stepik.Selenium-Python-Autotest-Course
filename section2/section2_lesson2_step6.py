from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/execute_script.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value") #находим значение x
    x = x_element.text #присваиваемм значение переменной x
    y = calc(x) #считаем математическую функцию для x

    # немного скроллим страницу вниз, что бы выполнить следующий код
    browser.execute_script("return arguments[0].scrollIntoView(true);", x_element)
    input_answer = browser.find_element(By.ID, "answer") #находим поле ввода мат. значения
    input_answer.send_keys(y) #вводим туда мат. x

    # чекбокс нашли по ID и проставили
    option_robotCheckbox = browser.find_element(By.ID, "robotCheckbox")
    option_robotCheckbox.click()
    # радио нашли по label и проставили
    option_robots_Rule = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    option_robots_Rule.click()

    # засабмитили болевым
    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()

finally:
    # успеваем скопировать код за 15 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
