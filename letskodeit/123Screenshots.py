from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://opensource-demo.orangehrmlive.com/")
usernameField = driver.find_element_by_id("txtUsername")
usernameField.click()
usernameField.send_keys("Admin")
passwordField = driver.find_element_by_id("txtPassword")
passwordField.click()
passwordField.send_keys("admin1234")
driver.find_element_by_id("btnLogin").click()
destinationFileName = "D:/Download/test.png"
try:
    driver.save_screenshot(destinationFileName)
    print("Screenshot saved to derectory -> " + destinationFileName)
except NotADirectoryError:
    print("Not a directory issue")

driver.quit()