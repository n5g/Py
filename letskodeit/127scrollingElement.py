from selenium import webdriver
import time
class ScrollingElement():

    def test(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://learn.letskodeit.com/p/practice")
        driver.implicitly_wait(3)
        #scroll down
        driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(2)
        #scrol up
        driver.execute_script("window.scrollBy(0, -1000);")
        time.sleep(2)
        #scroll element into view
        element = driver.find_element_by_id("mousehover")
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(2)
        driver.execute_script("window.scrollBy(0, -100);")
        #Native way ti scroll element into view
        time.sleep(3)
        driver.execute_script("window.scrollBy(0, -1000);")
        location = element.location_once_scrolled_into_view
        print("location: " + str(location))
        driver.quit()

run = ScrollingElement()
run.test()
