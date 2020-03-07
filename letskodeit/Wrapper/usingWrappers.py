from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from letskodeit.Wrapper.handyWrappers import HandyWrappers


class UsingWrapper():
    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)
        hw = HandyWrappers(driver)
        driver.get(baseUrl)


        textField1 = hw.getElement("name")
        textField1.send_keys("Test123")
        time.sleep(2)

        textField2 = hw.getElement("//input[@id='name']", locatorType="xpath")
        textField2.clear()
        driver.quit()

run = UsingWrapper()
run.test()