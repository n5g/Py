import time
from selenium import webdriver
import pytest

@pytest.fixture
def driver(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    request.addfinalizer(driver.quit)
    return driver

# def test_01_login_valid(driver):
#     driver.get("https://opensource-demo.orangehrmlive.com/")
#     driver.find_element_by_id("txtUsername").send_keys("Admin")
#     driver.find_element_by_id("txtPassword").send_keys("admin123")
#     driver.find_element_by_id("btnLogin").click()
#     time.sleep(2)
#     driver.find_element_by_id("welcome").click()
#     driver.find_element_by_link_text("Logout").click()

def test_02_login_invalid_username(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.find_element_by_id("txtUsername").send_keys("zxc")
    driver.find_element_by_id("txtPassword").send_keys("admin123")
    driver.find_element_by_id("btnLogin").click()
    actualString = driver.find_element_by_xpath("//span[@id='spanMessage']") #.getText()
    assert "Invalid credentials" in actualString





