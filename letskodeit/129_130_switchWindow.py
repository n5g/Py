from selenium import webdriver
import time
class SwitchWindow():

    def test(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://learn.letskodeit.com/p/practice")
        driver.implicitly_wait(3)

        #find parent handle -> main window
        parentHandle = driver.current_window_handle
        print("Parent handle: " + parentHandle)

        #find open window button and click it
        driver.find_element_by_id("openwindow").click()
        time.sleep(2)
        #find all handles, there should two handles after
        handles = driver.window_handles
        #switch to window and search course
        for handle in handles:
            print("Handle: " + handle)
            if handle not in parentHandle:
                driver.switch_to.window(handle)
                print("Switched to window: " + handle)
                searchBox = driver.find_element_by_id("search-courses")
                searchBox.send_keys("python")
                time.sleep(4)
                driver.close()
                break
         #switch back to the parent handle
        driver.switch_to.window(parentHandle)
        time.sleep(2)
        driver.find_element_by_id("name").send_keys("Test successful")
        time.sleep(4)
        driver.quit()


run = SwitchWindow()
run.test()
