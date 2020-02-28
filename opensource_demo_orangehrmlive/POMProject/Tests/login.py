import time
from selenium import webdriver
import unittest
from opensource_demo_orangehrmlive.POMProject.Pages.loginPage import LoginPage
from opensource_demo_orangehrmlive.POMProject.Pages.homePage import HomePage

class LoinTest(unittest.TestCase):

    @classmethod
    def setUp(Self):
        Self.driver = webdriver.Chrome()
        Self.driver.implicitly_wait(5)
        Self.driver.maximize_window()


    def test_01_login_valid(self):
        driver = self.driver

        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePage(driver)
        time.sleep(2)
        homepage.click_welcome()
        homepage.click_logout()

    @classmethod
    def tearDown(self):
        self.driver.quit()
        print("Test completed")

if __name__ == '__main__':
    unittest.main()



