from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # напшли и прописали данные
    input_first_name = browser.find_element(By.NAME, 'firstname')
    input_first_name.send_keys("Ivan")
    input_last_name = browser.find_element(By.NAME, 'lastname')
    input_last_name.send_keys("Petrov")
    input_email = browser.find_element(By.NAME, 'email')
    input_email.send_keys("test@stopik.by")

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'izdomu.txt')     # добавляем к этому пути имя файла

    file_kickass = browser.find_element(By.ID, 'file')  # находим кнопку отправки файла
    file_kickass.send_keys(file_path)   # пинаем-отправляем файл

    # нашли и засабмитили
    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
