from letskodeit.letskodeit_POM.base.selenium_driver import SeleniumDriver

class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    #нужня для того чтобы поменять локатор только тут а не в самих методах
    _login_link = "Login"
    _email_field = "user_email"
    _password_field = "user_password"
    _login_button = "commit"

    def getLoginLink(self):
        return self.driver.find_element_by_link_text(self._login_link)

    def getEmailField(self):
        return self.driver.find_element_by_id(self._email_field)

    def getPasswordField(self):
        return self.driver.find_element_by_id(self._password_field)

    def getLoginButton(self):
        return self.driver.find_element_by_name(self._login_button)

    def clickLoginLink(self):
        self.getLoginLink().click()

    def enterEmail(self, email):                 #email аргумент
        self.getEmailField().send_keys(email)    #email дата

    def enterPassword(self, password):
        self.getPasswordField().send_keys(password)

    def clickLoginButton(self):
        self.getLoginButton().click()

    def login(self, email, password):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()