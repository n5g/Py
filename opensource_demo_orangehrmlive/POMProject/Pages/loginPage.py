from opensource_demo_orangehrmlive.POMProject.Locators.locators import Locators
class LoginPage():
    def __init__(self, driver):
        self.driver = driver

        #self.invalidUsername_message_xpath = "//span[@id='spanMessage']"

    def enter_username(self, username):
        self.driver.find_element_by_id(Locators.username_textbox_id).clear()
        self.driver.find_element_by_id(Locators.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(Locators.password_textbox_id).clear()
        self.driver.find_element_by_id(Locators.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id(Locators.login_button_id).click()

    def check_invalid_username_massage(self, message):
        #msg = self.driver.find_element_by_xpath(self.invalidUsername_message_xpath).text
        self.driver.find_element_by_xpath(Locators.invalidUsername_message_xpath).text
        #return msg
