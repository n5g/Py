from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from letskodeit.Wrapper import HandyWrapper


class UsingWrapper():
    def test(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(2)
        driver.get("https://learn.letskodeit.com/p/practice")
        hw = HandyWrapper(driver)

        textField1 = hw.getElement("name")
        textField1.send_keys("Test123")

        time.sleep(2)
        textField2 = hw.getElement("/input[@id='name']", locatorType="xpath")
        textField2.clear()
        driver.quit()

run = UsingWrapper()
run.test()