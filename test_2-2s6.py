import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    url = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(url)

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    browser.execute_script("window.scrollBy(0, 100);")

    answer_input = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer_input.send_keys(y)

    checkbox_robot = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox_robot.click()

    radiobutton_robot = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radiobutton_robot.click()

    submit_button = browser.find_element(By.CSS_SELECTOR, ".btn")
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()
