from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
#link = "http://suninjuly.github.io/selects2.html"

def sum(a, b):
    return a + b

try:
    browser = webdriver.Chrome()
    browser.get(link)
    # получаем в x и y спрятанное значение
    x_element = browser.find_element(By.ID, 'num1')
    x = int(x_element.text)
    #print(x)
    y_element = browser.find_element(By.ID, 'num2')
    y = int(y_element.text)
    #print(y)
    # складываем x+y через sum
    z = str(sum(x, y))
    #print(z)

    select = Select(browser.find_element(By.ID, ('dropdown'))) # находим список
    select.select_by_value(z) # в списке находим значение равное сумме (z)
    time.sleep(1)

    # засабмитили болевым
    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()

finally:
    # успеваем скопировать код за 15 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

