from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):

    def is_login_url(self):
        assert 'login' in self.browser.current_url, "NO 'login' in URL"
    
    def is_login_form(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL_INPUT), "NO email input for Log In found"
        assert self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD_INPUT), "NO password input for Log In found"
    
    def is_registration_form(self):
        assert self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL_INPUT), "NO email input for Registration found"
        assert self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_INPUT), "NO first password input for Registration found"
        assert self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_REPEAT), "NO second password input for Registration found"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL_INPUT).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_INPUT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_REPEAT).send_keys(password)

        self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON).click()