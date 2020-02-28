import time
from selenium import webdriver
import unittest

class LoinTest(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def test_01_login_valid(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()
        time.sleep(3)
        self.driver.find_element_by_id("welcome").click()
        self.driver.find_element_by_link_text("Logout").click()
        #time.sleep(3)

    @classmethod
    def tearDown(self):
        self.driver.quit()
        print("Test completed")

if __name__ == '__main__':
    unittest.main()



