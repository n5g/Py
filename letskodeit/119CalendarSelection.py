from selenium import webdriver
import time

class CalendarSelection():

    def test1(self):
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

    def test2(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get("https://www.expedia.com/")
        driver.find_element_by_id("tab-flight-tab-hp").click()
        departingField = driver.find_element_by_id("flight-departing-hp-flight")
        departingField.click()
        # Выбрать дату из календаря
        #//div[@class='datepicker-cal-month'][position()=1]//td выбрат 1 секцию календаря
        calMonth = driver.find_element_by_xpath("//div[@class='datepicker-cal-month'][position()=1]")
        allValidDates = calMonth.find_elements_by_tag_name("button")
        time.sleep(2)
        for date in allValidDates:
            if date.text == " 31":
                date.click()
                break
        time.sleep(2)
        driver.quit()


run = CalendarSelection()
run.test2()

