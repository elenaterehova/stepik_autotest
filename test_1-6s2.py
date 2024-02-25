from selenium import webdriver
from selenium.webdriver.common.by import By

url = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(url)
    button = browser.find_element(By.ID, "submit_button")
    button.click()
finally:
    browser.quit()
