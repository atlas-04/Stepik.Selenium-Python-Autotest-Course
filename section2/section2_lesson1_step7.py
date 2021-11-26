from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    # получаем в x спрятанное значение
    x_element = browser.find_element(By.ID, "treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)

    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(y)
    
    # чекбокс нашли по ID и проставили
    option_robotCheckbox = browser.find_element(By.ID, "robotCheckbox")
    option_robotCheckbox.click()
    robots_checked = option_robotCheckbox.get_attribute("checked")
    assert robots_checked is not None
    
    # радио нашли по label и проставили
    option_people_Rule = browser.find_element(By.ID, "peopleRule")
    ch_option_people_Rule = option_people_Rule.get_attribute("checked")
    print("value of people radio: ", ch_option_people_Rule)
    assert ch_option_people_Rule is not None, "People radio is not selected by default"
    option_robots_Rule = browser.find_element(By.ID, "robotsRule")
    option_robots_Rule.click()
    
    # засабмитили болевым
    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()

finally:
    # успеваем скопировать код за 15 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

