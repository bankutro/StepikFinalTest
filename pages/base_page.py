from selenium.common.exceptions import NoSuchElementException

class BasePage():

    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.timeout = timeout

    def open(self):
        self.browser.implicitly_wait(self.timeout)
        self.browser.get(self.url)

    def is_element_present(self, selector_type, selector):
        try:
            self.browser.find_element(selector_type, selector)
        except (NoSuchElementException):
            return False
        return True