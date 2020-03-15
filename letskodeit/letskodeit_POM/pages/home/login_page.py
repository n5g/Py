from letskodeit.letskodeit_POM.base.selenium_driver import SeleniumDriver
import letskodeit.letskodeit_POM.utillities.custom_logger as cl
import logging

class LoginPage(SeleniumDriver):
    log = cl.customLogge(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    #нужня для того чтобы поменять локатор только тут а не в самих методах
    _login_link = "Login"
    _email_field = "user_email"
    _password_field = "user_password"
    _login_button = "commit"

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="link")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="name")

    def login(self, email='', password=''):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("//span[@class='navbar-current-user']",locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//div[cotains(text(),'Invalid email or password')]", locatorType="xpath")
        return result
