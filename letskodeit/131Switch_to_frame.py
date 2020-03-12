from selenium import webdriver
import time
class SwitchToFrame():

    def test(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://learn.letskodeit.com/p/practice")
        driver.implicitly_wait(3)
        driver.execute_script("window.scrollBy(0, 1000);")
        #Switch to frame using id
        #driver.switch_to.frame("courses-iframe")
        #switch to frame using name
        #driver.switch_to.frame("iframe - name")
        #switch to frame using numbers
        driver.switch_to.frame(0)
        #search course
        searchBox = driver.find_element_by_id("search-courses")
        searchBox.send_keys("python")
        time.sleep(2)

        #switch back to the parent frame
        driver.switch_to.default_content()
        driver.execute_script("window.scrollBy(0, -1000);")
        time.sleep(3)
        driver.find_element_by_name("enter-name").send_keys("Test successful")
        time.sleep(3)
        driver.quit()

run = SwitchToFrame()
run.test()
