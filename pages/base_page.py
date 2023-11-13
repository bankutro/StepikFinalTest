from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .locators import BasePageLocators
import math

class BasePage():

    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.timeout = timeout

    def go_to_login_page(self):
        self.browser.find_element(*BasePageLocators.LOGIN_LINK).click()

    def is_login_link(self):
        assert self.browser.find_element(*BasePageLocators.LOGIN_LINK), "NO login link has been found"

    def is_element_present(self, selector_type, selector):
        try:
            self.browser.find_element(selector_type, selector)
        except (NoSuchElementException):
            return False
        return True
    
    def is_not_element_present(self, selector_type, selector, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((selector_type, selector)))
        except TimeoutException:
            return True
        return False
    
    def is_disappeared(self, locator_type, locator, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((locator_type, locator)))
        except TimeoutError:
            return False
        return True
    
    def open(self):
        self.browser.implicitly_wait(self.timeout)
        self.browser.get(self.url)

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")