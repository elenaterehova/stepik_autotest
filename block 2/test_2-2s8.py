import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    url = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(url)

    first_name = browser.find_element(By.NAME, "firstname")
    first_name.send_keys('first name')

    last_name = browser.find_element(By.NAME, "lastname")
    last_name.send_keys('Last name')

    email = browser.find_element(By.NAME, "email")
    email.send_keys('email@mail.ru')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test_2-2s8.txt')

    input_file = browser.find_element(By.CSS_SELECTOR, "#file")
    input_file.send_keys(file_path)

    submit_button = browser.find_element(By.CSS_SELECTOR, ".btn")
    submit_button.click()

finally:
    time.sleep(5)
    browser.quit()