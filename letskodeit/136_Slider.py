from selenium import webdriver
import time
from selenium.webdriver import ActionChains
class Slider():

    def test(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://jqueryui.com/slider")
        driver.implicitly_wait(3)
        driver.switch_to.frame(0)
        element = driver.find_element_by_xpath("//div[@id='slider']//span")
        time.sleep(2)
        try:
            actions = ActionChains(driver)
            actions.drag_and_drop_by_offset(element, 100, 0).perform()
            print("Sliding element successful")
            time.sleep(2)
        except:
            print("Sliding failed on element")
        driver.quit()

run = Slider()
run.test()