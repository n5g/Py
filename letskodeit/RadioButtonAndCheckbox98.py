from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://learn.letskodeit.com/p/practice")
# bmwRadioBtn = driver.find_element_by_id("bmwradio")
# bmwRadioBtn.click()
# time.sleep(2)
# driver.find_element_by_id("benzradio").click()
# bmwCheckBox = driver.find_element_by_id("bmwcheck")
# bmwCheckBox.click()
# driver.find_element_by_id("benzcheck").click()
# time.sleep(3)
# #true is selected. false is notselected
# print("BMW radio button is selected? "+ str(bmwRadioBtn.is_selected()))
# print("benzcheckbox radio button is selected? "+ str(bmwCheckBox.is_selected()))
#
#99 lesson elements list
radioButtonsList = driver.find_elements_by_xpath("//input[@type='radio']")
size = len(radioButtonsList)
print("Size of the list: " + str(size))
for radioButton in radioButtonsList:
    isSelected = radioButton.is_selected()
    if not isSelected:
        radioButton.click()
#101
element = driver.find_element_by_id("carselect")
sel = Select(element)
sel.select_by_value("benz")
print("select benz by value")
time.sleep(2)
sel.select_by_index("2")
print("select honda by index")
time.sleep(2)
sel.select_by_visible_text("BMW")
print("select bmw by visible text")
time.sleep(2)
sel.select_by_index("2")
print("select honda y index")

driver.quit()

