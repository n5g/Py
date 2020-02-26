import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def driver(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(2)
    request.addfinalizer(driver.quit)
    return driver


def test_yandex_search(driver):
    driver.get("https://yandex.ru/")
    search_input = driver.find_element_by_xpath("//input[@id='text']")
    search_input.send_keys("yandex market")
    search_button = driver.find_element_by_xpath("//button[@type='submit']")
    search_input.click()

    def check_results_count(driver):
        inner_search_results = driver.find_element_by_xpath("//li[@class='serp-item']")
        return len(inner_search_results) == 11

    # ("//div[@class='organic__url-text']")
    # ("//li[@class='serp-item']")
    search_results = driver.find_elements_by_xpath("//li[@class='serp-item']")
    link = search_results[2].find_element_by_xpath("//h2/a")
   # link.click()
    #driver.switch_to_window(driver.window_handles[1])
