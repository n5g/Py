from selenium import webdriver
import time
from selenium.webdriver import ActionChains
class MouseHovering():

    def test(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://learn.letskodeit.com/p/practice")
        driver.implicitly_wait(3)
        driver.execute_script("window.scrollBy(0, 800);")
        element = driver.find_element_by_id("mousehover")
        time.sleep(2)
        itemToClickLocator = "//div[@class='mouse-hover-content']//a[text()='Top']"

        try:
            action = ActionChains(driver)
            action.move_to_element(element).perform()
            print("Mouse Hovered on element")
            time.sleep(2)
            topLink = driver.find_element_by_xpath(itemToClickLocator)
            action.move_to_element(topLink).click().perform()
            print("Item clicked")
            time.sleep(2)
        except:
            print("mouse hover failed on element")

run = MouseHovering()
run.test()