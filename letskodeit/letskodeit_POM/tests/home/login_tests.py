from selenium import webdriver
from letskodeit.letskodeit_POM.pages.home.login_page import LoginPage
import unittest
import pytest

class LoginTests(unittest.TestCase):
    baseURL = "https://letskodeit.teachable.com/"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get(baseURL)
    lp = LoginPage(driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("test@email.com", "abcabc")
        result = self.lp.verifyLoginSuccessful()
        assert result == True
        self.driver.quit()

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.driver.get(self.baseURL)
        self.lp.login("test@email.com", "abcabcabcabc")
        result = self.lp.verifyLoginFailed()
        assert result == True



