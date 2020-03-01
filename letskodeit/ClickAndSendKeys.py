from selenium import webdriver
import time


class ClickAndSendKeys():
    def test(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get("https://learn.letskodeit.com/")
        loginLink = driver.find_element_by_xpath('//a[@href="/sign_in"]')
        loginLink.click()

        emailField = driver.find_element_by_id('user_email')
        emailField.send_keys("test")

        passwordField = driver.find_element_by_id('user_password')
        passwordField.send_keys("test")

        time.sleep(2)
        emailField.clear()
        time.sleep(2)
        emailField.send_keys("test")
        driver.quit()


ff = ClickAndSendKeys()
ff.test()
