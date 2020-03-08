from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://www.southwest.com/")
cityField = driver.find_element_by_id("LandingAirBookingSearchForm_originationAirportCode")
cityField.send_keys("New York")
# "//ul[@id='air-city-departuremenu']//li[contains(text), 'NJ - LGA')]"
time.sleep(2)










