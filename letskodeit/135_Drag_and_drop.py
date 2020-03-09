from selenium import webdriver
import time
from selenium.webdriver import ActionChains
class DragAndDrop():

    def test(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://jqueryui.com/droppable/")
        driver.implicitly_wait(3)
        driver.switch_to.frame(0)

        fromElement = driver.find_element_by_id("draggable")
        toElement = driver.find_element_by_id("droppable")
        time.sleep(2)
        try:
            actions = ActionChains(driver)
            #actions.drag_and_drop(fromElement, toElement).perform()
            # тоже самое что и выше
            actions.click_and_hold(fromElement).move_to_element(toElement).release().perform()
            print("Drag and drop element successful")
            time.sleep(2)
        except:
            print("drag and drop failed on element")
        driver.quit()
run = DragAndDrop()
run.test()