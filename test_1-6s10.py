import time

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    url = "http://suninjuly.github.io/registration2.html"

    browser = webdriver.Chrome()
    browser.get(url)

    first_name = browser.find_element(By.XPATH, "//input[contains(@class, 'first') and @required]")
    first_name.send_keys('text')
    last_name = browser.find_element(By.XPATH, "//input[contains(@class, 'second') and @required]")
    last_name.send_keys('text')
    email = browser.find_element(By.XPATH, "//input[contains(@class, 'third') and @required]")
    email.send_keys('text')

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    time.sleep(10)
    browser.quit()