from selenium import webdriver
import time

class FindIdName():
    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome()
        driver.get(baseUrl)
        elementById = driver.find_element_by_id("name")

        if elementById is not None:
            print("We found an element by id")
        elementByName = driver.find_element_by_name("show-hide")
        if elementByName is not None:
            print("We found an element by name")
        elementByXpath = driver.find_element_by_xpath("//input[@id='name']")
        if elementByXpath is not None:
            print("We found an element by xpath")
        elementByCSS = driver.find_element_by_css_selector("#displayed-text")
        if elementByCSS is not None:
            print("We found an element by css")
        elementByLinkText = driver.find_element_by_link_text("Login")
        if elementByCSS is not None:
            print("We found an element by link text")
        elementByPatiallLinkText = driver.find_element_by_partial_link_text("Pract")
        if elementByCSS is not None:
            print("We found an element by partial link text")
        elementByClassName = driver.find_element_by_class_name("displayed-class")
        if elementByClassName is not None:
            print("We found an element by class name")
        elementByTagName = driver.find_element_by_tag_name("h1")
        text = elementByTagName.text
        if elementByTagName is not None:
            print("We found an element by tag name and yhe text on element: "+ text)
        time.sleep(2)
        driver.quit()


ff = FindIdName()
ff.test()