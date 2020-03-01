from selenium import webdriver
import time

class BrowserInteractions():
    def test(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://learn.letskodeit.com/p/practice")
        title = driver.title
        print("Title of the page is: " + title)
        currentUrl = driver.current_url
        print("Current url of the web page is: " + currentUrl)
        driver.refresh()
        print("Browser refreshed 1st time")
        driver.get(driver.current_url)
        print("Browser refreshed 2st time")
        driver.get("https://sso.teachable.com/secure/42299/users/sign_in?clean_login=true&reset_purchase_session=1")
        currentUrl = driver.current_url 
        print("Current url of the web page is: " + currentUrl)
        driver.back()
        driver.forward()
        pageSource = driver.page_source
        driver.close()
        driver.quit()

ff = BrowserInteractions()
ff.test()
