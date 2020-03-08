from selenium import webdriver
import time
from selenium.webdriver.common.by import By
class Screenshots():

    def test(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        #driver.get("https://learn.letskodeit.com/p/practice")
        #Открываем стрвницу этой командой
        driver.execute_script("window.location = 'https://learn.letskodeit.com/p/practice';")
        driver.implicitly_wait(5)
        #element = driver.find_element(By.ID, "name")
        element = driver.execute_script("return document.getElementById('name');")
        element.send_keys("Test")
        time.sleep(4)
        driver.quit()

run = Screenshots()
run.test()