from selenium import webdriver
from selenium.webdriver.common.by import By

class FindBy():
    def test(self):
        driver = webdriver.Chrome()
        driver.get("https://learn.letskodeit.com/p/practice")

        elementById = driver.find_element(By.ID, "name")
        if elementById is not None:
            print("We found an element by id")
        elementByXpath = driver.find_element(By.XPATH, "//input[@id='displayed-text']")
        if elementByXpath is not None:
            print("We found an element by xpath")
        elementByLinkText = driver.find_element(By.LINK_TEXT, "Login")
        if elementByLinkText is not None:
             print("We found an element by link text")

ff = FindBy()
ff.test()