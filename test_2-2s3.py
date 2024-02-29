import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def summ(x, y):
    return str(x + y)


try:
    url = "http://suninjuly.github.io/selects1.html"

    browser = webdriver.Chrome()
    browser.get(url)

    num1 = browser.find_element(By.CSS_SELECTOR, "#num1")
    x = int(num1.text)
    num2 = browser.find_element(By.CSS_SELECTOR, "#num2")
    y = int(num2.text)

    sum = summ(x, y)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(sum)

    submit_button = browser.find_element(By.CSS_SELECTOR, ".btn")
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()
