from selenium import webdriver
import time

baseURL = "https://letskodeit.teachable.com/"
baseURL2 = "https://sso.teachable.com/secure/42299/users/sign_in?clean_login=true&reset_purchase_session=1"
baseURL3 = "https://learn.letskodeit.com/?_ga=2.177656805.1910616277.1584125361-225475664.1583002049"
driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(3)
driver.get(baseURL3)

loginLink = driver.find_element_by_link_text("Login")
loginLink.click()
time.sleep(4)


driver.quit()