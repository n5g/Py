from selenium import webdriver
import time

class HiddenElements():

    def testLetsKodeIt(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(2)


        # Find the state of the text box
        textBoxElement = driver.find_element_by_id("displayed-text")
        textBoxState = textBoxElement.is_displayed() # True if visible, False if hidden
        # Exception if not present in the DOM
        print("Text is visible? " + str(textBoxState))
        time.sleep(2)

        # Click the Hide button
        driver.find_element_by_id("hide-textbox").click()
        # Find the state of the text box
        textBoxState = textBoxElement.is_displayed()
        print("Text is visible ? " + str(textBoxState))
        time.sleep(2)
        # Click the Show button
        driver.find_element_by_id("show-textbox").click()
        # Find the state of the text box
        textBoxState = textBoxElement.is_displayed()
        print("Text is visible? " + str(textBoxState))
        time.sleep(2)
        # Browser Close
        driver.quit()


run = HiddenElements()
run.testLetsKodeIt()
