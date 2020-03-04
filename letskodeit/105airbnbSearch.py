from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://www.airbnb.ru/")
serchfield = driver.find_element_by_xpath("//input[@name='query']")
#serchfield.click()
serchfield.send_keys("ufa russia")
time.sleep(2)
serchfield.send_keys(Keys.Enter)
#arrivalField = driver.find_element_by_id("checkin_input")
#arrivalField.click()
#sel = Select(arrivalField)
#sel.select_by_visible_text("17")
driver.find_element_by_xpath("//td[@class='_f6dv71o']").click()
time.sleep(3)
driver.quit()
