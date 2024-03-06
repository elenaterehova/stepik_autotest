import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    url = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(url)

    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

    alert = browser.switch_to.alert
    alert.accept()

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    answer_input = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer_input.send_keys(y)

    submit_button = browser.find_element(By.CSS_SELECTOR, ".btn")
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()
