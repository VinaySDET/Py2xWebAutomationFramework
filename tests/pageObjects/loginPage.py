# Page Class
# Page Locators
# Page Actions
# Webdriver Init
# Custom Functions
# No assertions (in Page Object Class)

# * What exactly this function does and what's the responsibility of the LoginPage class?
# * Responsibility:
# * 1. get username, send keys --> email address
# * 2. get password, send keys --> email address
# * 3. click on the submit button and navigate to dashboard page.
# * 4. Invalid --> error message
# * 5. Forgot Password

from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    # * Page Locators
    username = (By.XPATH, "//input[@id='login-username']")
    password = (By.XPATH, "//input[@id='login-password']")
    submit_button = (By.XPATH, "//button[@id='js-login-btn']")
    # forgot_password_button=(By.XPATH,"//button[normalize-space()='Forgot Password?']")
    error_message = (By.XPATH, "//div[@id='js-notification-box-msg']")

    # free_trail=(By.XPATH,"//a[normalize-space()='Start a free trial']")
    # sso_login=(By.XPATH,"//button[normalize-space()='Sign in using SSO']")
    # remember_checkbox=(By.XPATH,"//input[@id='checkbox-remember']")

    # * Page Actions
    def get_username(self):
        return self.driver.find_element(*LoginPage.username)

    def get_password(self):
        return self.driver.find_element(*LoginPage.password)

    def get_submit_button(self):
        return self.driver.find_element(*LoginPage.submit_button)

    # def get_forgot_password_button(self):
    #     return self.driver.find_element(*LoginPage.forgot_password_button)

    def get_error_message(self):
        return self.driver.find_element(*LoginPage.error_message)

    # def get_free_trail(self):
    #     return self.driver.find_element(*LoginPage.free_trail)
    #
    # def get_sso_login(self):
    #     return self.driver.find_element(*LoginPage.sso_login)
    #
    # def get_remember_checkbox(self):
    #     return self.driver.find_element(*LoginPage.remember_checkbox)

    # * Page Actions - Main Actions
    def login_to_vwo(self, usr, pwd):
        self.get_username().send_keys(usr)
        self.get_password().send_keys(pwd)
        self.get_submit_button().click()

    def get_error_message_text(self):
        return self.get_error_message().text

    # def get_free_trail_message_text(self):
    #     return self.driver.find_element_by_id(self.get_free_trail_message()).click()

    # def get_sso_login_text(self):
    #     return self.driver.find_element_by_id(self.get_sso_login()).click()
