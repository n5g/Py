from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://www.google.com")
e1 = driver.find_element_by_name("q")
e1State = e1.is_enabled()   # узнать доступен ли элемент?
print("E1 is Enabled? -> " +str(e1State))
e1.send_keys("letskodeit")
time.sleep(3)
driver.quit()
