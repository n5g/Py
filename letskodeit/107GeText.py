from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(2)
driver.get("https://learn.letskodeit.com/p/practice")
openTabElement = driver.find_element_by_id("opentab")
elementText = openTabElement.text
print("Text on element is: " + elementText)

#get attribute 108
element = driver.find_element_by_id("name")
result = element.get_attribute("class")
result2 = element.get_attribute("type")
print("value of attribue  is: " + result)
print("value2 of attribue is: " + result2)






driver.quit()
