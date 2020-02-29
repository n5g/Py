import time
from selenium import webdriver
import pytest
from opensource_demo_orangehrmlive.POMProject.Pages.loginPage import LoginPage
from opensource_demo_orangehrmlive.POMProject.Pages.homePage import HomePage


@pytest.fixture
def driver(self):
    driver = webdriver.Chrome()
    self.addfinalizer(driver.quit)
    driver.implicitly_wait(5)
    driver.maximize_window()
    return driver

    # def test_01_login_valid(self):
    #     driver = self.driver
    #
    #     driver.get("https://opensource-demo.orangehrmlive.com/")
    #
    #     login = LoginPage(driver)
    #     login.enter_username("Admin")
    #     login.enter_password("admin123")
    #     login.click_login()
    #
    #     homepage = HomePage(driver)
    #     time.sleep(2)
    #     homepage.click_welcome()
    #     homepage.click_logout()

def test_02_login_invalid_username(self):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    login = LoginPage(driver)
    login.enter_username("Admin1")
    login.enter_password("admin123")
    login.click_login()
    message = driver.find_element_by_xpath("//span[@id='spanMessage']").text
    self.assertEqual(message, "Invalid credentials")





