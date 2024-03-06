import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url1 = "http://suninjuly.github.io/registration1.html"
url2 = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()


class TestStep1(unittest.TestCase):
    def test_registration1(self):
        browser.get(url1)

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

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_registration2(self):
        browser.get(url2)

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

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)


if __name__ == "__main__":
    unittest.main()
