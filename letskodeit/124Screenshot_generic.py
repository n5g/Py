from selenium import webdriver
import time
class Screenshots():

    def test(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(2)
        driver.get("https://opensource-demo.orangehrmlive.com/")
        usernameField = driver.find_element_by_id("txtUsername")
        usernameField.click()
        usernameField.send_keys("Admin")
        passwordField = driver.find_element_by_id("txtPassword")
        passwordField.click()
        passwordField.send_keys("admin1234")
        driver.find_element_by_id("btnLogin").click()
        self.takeScreenshot(driver)
        driver.quit()



    def takeScreenshot(self, driver):
        #Take screenshot of the current open web page
        #param driver
        #return

        fileName = str(round(time.time() * 1000)) + ".png"
        screenshotDirectoy = "D:/Download/"
        destinationFile = screenshotDirectoy + fileName

        try:
            driver.save_screenshot(destinationFile)
            print("Screenshot saved to derectory -> " + destinationFile)
        except NotADirectoryError:
            print("Not a directory issue")

run = Screenshots()
run.test()
