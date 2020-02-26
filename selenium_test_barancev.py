import pytest
from selenium import webdriver
import selenium
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    print(wd.capabilities) #узнать настройки браузера
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("http://www.google.com/")
    search_button = driver.find_element_by_name("q")
    search_button.send_keys("webdriver")
    search_button.send_keys(Keys.ENTER)
    time.sleep(2)

    #driver.find_element_by_xpath("//div[@class='tfB0Bf']//input[@name='btnK']").click()
    #WebDriverWait(driver, 10).until(EC.title_is("webdriver - Поиск в Google"))