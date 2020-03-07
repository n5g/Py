from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://www.expedia.com/")
driver.find_element_by_id("tab-flight-tab-hp").click()
departingField = driver.find_element_by_id("flight-departing-hp-flight")
departingField.click()
#Выбрать дату из календаря
dateToSelect = driver.find_element_by_xpath("//button[@class='datepicker-cal-date' and @data-day='28' and @data-month='2' ]")
dateToSelect.click()
time.sleep(5)
driver.quit()