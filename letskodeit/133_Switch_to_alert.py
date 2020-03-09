from selenium import webdriver
import time
class SwitchToAlert():

    def test(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://learn.letskodeit.com/p/practice")
        driver.implicitly_wait(3)
        driver.find_element_by_id("name").send_keys("Ed")
        driver.find_element_by_id("alertbtn").click()
        time.sleep(2)
        alert1 = driver.switch_to.alert
        alert1.accept() #есть только кнопка ОК,у нее нет тега, т.к это джава скрипт
        time.sleep(2)
        driver.find_element_by_id("confirmbtn").click()
        time.sleep(2)
        alert2 = driver.switch_to.alert
        alert2.dismiss() #тут есть 2 кнопки ок и cancel. Нажать На сancel
        time.sleep(2)
        driver.quit()

run = SwitchToAlert()
run.test()






