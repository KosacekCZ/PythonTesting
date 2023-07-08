from unittest import TestCase
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

class TestWebTest(TestCase):
    def test_zkouska_wikipedie(self):
        driver = webdriver.Chrome()

        self.driver.get("https://www.wikipedia.org")

        time.sleep(1)

        self.driver.find_element(By.NAME, "search").send_keys("Python")
        time.sleep(0.5)
        self.driver.find_element(By.NAME, "search").send_keys(Keys.ENTER)

        time.sleep(10)

