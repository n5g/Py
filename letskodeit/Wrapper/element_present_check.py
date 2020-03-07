from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from letskodeit.Wrapper.handyWrappers import HandyWrappers


class ElementPresentCheck():
    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)
        hw = HandyWrappers(driver)
        driver.get(baseUrl)

        elementResult1 = hw.isElementPresent("name", By.ID)
        print(str(elementResult1))

        elementResult2 = hw.elementPresentsCheck("//input[@id='name']", By.XPATH)
        print(str(elementResult2))

run = ElementPresentCheck()
run.test()
