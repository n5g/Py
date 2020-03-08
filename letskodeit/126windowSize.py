from selenium import webdriver
import time
class Screenshots():

    def test(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        #driver.get("https://learn.letskodeit.com/p/practice")
        driver.implicitly_wait(3)

        height = driver.execute_script("return window.innerHeight;")
        width = driver.execute_script("return window.innerWidth;")
        print("Height: " + str(height))
        print("Width: " + str(width))
        driver.quit()

run = Screenshots()
run.test()