import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#@pytest.fixture(scope="function")
#def browser():
#    print("\nstart browser for test..")
#    browser = webdriver.Chrome()
#    yield browser
#   print("\nquit browser..")
#    browser.quit()


@pytest.mark.parametrize('linkplus', ["236895", "236896", "236897","236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, linkplus):
    # открываем линк, находим поле, кликаем, вписываем ответ (answer(время с тачки))
    link = f"https://stepik.org/lesson/{linkplus}/step/1"
    browser.get(link)
    browser.implicitly_wait(10) # дабы не тайм слип везде
    answer = str(math.log(int(time.time()))) # фикстурой не получилось, str для скрипта
    ember = WebDriverWait(browser, 1).until(EC.element_to_be_clickable ((By.CSS_SELECTOR, ".show-plugin .ember-text-area")))
    ember.click()
    ember.send_keys(answer)

    # засабмитили болевым
    button = WebDriverWait(browser, 1).until(EC.element_to_be_clickable ((By.XPATH, "//section/div/div[1]/div[4]/button")))
    button.click()

    x = WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.XPATH, "//div/pre")))
    correct_text = x.get_attribute('innerHTML')
    assert correct_text == 'Correct!' 
