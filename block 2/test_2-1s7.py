import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    url = "http://suninjuly.github.io/get_attribute.html"

    browser = webdriver.Chrome()
    browser.get(url)

    treasure_img = browser.find_element(By.CSS_SELECTOR, "img")
    x = treasure_img.get_attribute("valuex")
    y = calc(x)

    answer_field = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer_field.send_keys(y)

    robot_checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    robot_checkbox.click()

    robot_radiobutton = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    robot_radiobutton.click()

    submit_button = browser.find_element(By.CSS_SELECTOR, ".btn")
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()
