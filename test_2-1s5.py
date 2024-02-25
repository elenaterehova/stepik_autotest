import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    url = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(url)

    x_element= browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    input_field = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_field.send_keys(y)

    chbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    chbox.click()

    radiobtn = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radiobtn.click()

    submit_button = browser.find_element(By.CSS_SELECTOR, ".btn")
    submit_button.click()

    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()
