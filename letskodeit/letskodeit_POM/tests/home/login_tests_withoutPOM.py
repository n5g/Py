from selenium import webdriver

class LoginTests():

    def test_validLogin(self):
        baseURL = "https://letskodeit.teachable.com/"
        baseURL2 = "https://sso.teachable.com/secure/teachable_accounts/sign_in"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL2)

        # loginLink = driver.find_element_by_link_text("Login")
        # loginLink.click()

        emailField = driver.find_element_by_id("user_email")
        emailField.send_keys("test@email.com")

        passwordField = driver.find_element_by_id("user_password")
        passwordField.send_keys("abcabc")

        loginButton = driver.find_element_by_name("commit")
        loginButton.click()

        userIcon = driver.find_element_by_xpath("//span[@class='navbar-current-user']")
        if userIcon is not None:
            print("Login successful")
        else:
            print("Login Failed")

        driver.quit()


run = LoginTests()
run.test_validLogin()