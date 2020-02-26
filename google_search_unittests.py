from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.keys import Keys

class google_search(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://google.com")

    def test_01_search(self):
        driver = self.driver
        input_field = driver.find_element_by_name("q")
        input_field.send_keys("python")
        input_field.send_keys(Keys.ENTER)
        time.sleep(2)
        titles = driver.find_elements_by_class_name("LC20lb DKV0Md")
        for title in titles:
            assert "python" in title.text.lower()

    def test_02_search(self):
        driver = self.driver
        input_field = driver.find_element_by_name("q")
        input_field.send_keys("python")
        time.sleep(1)
        input_field.send_keys(Keys.ARROW_DOWN)
        input_field.send_keys(Keys.ENTER)
        time.sleep(1)
        titles = driver.find_elements_by_class_name("LC20lb DKV0Md")
        for title in titles:
            assert "python" in title.text.lower()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

