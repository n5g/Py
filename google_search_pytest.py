import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def driver(request):
    driver = webdriver.Chrome()
    request.addfinalizer(driver.quit)
    return driver

def test_01_search(driver):
    driver.get("http://www.google.com/")
    input_field = driver.find_element_by_name("q")
    input_field.send_keys("python")
    input_field.send_keys(Keys.ENTER)
    time.sleep(1)
    titles = driver.find_elements_by_class_name("LC20lb DKV0Md")
    for title in titles:
        assert "python" in title.text.lower()

def test_02_search(driver):
    driver.get("http://www.google.com/")
    input_field = driver.find_element_by_name("q")
    input_field.send_keys("python" +Keys.ARROW_DOWN + Keys.ENTER)
    time.sleep(1)
    titles = driver.find_elements_by_class_name("LC20lb DKV0Md")
    for title in titles:
        assert "python" in title.text.lower()


