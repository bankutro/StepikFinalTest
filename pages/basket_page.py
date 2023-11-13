from .base_page import BasePage
from .locators import BasketLocators

class BasketPage(BasePage):

    def is_basket_empty(self):
        self.is_not_element_present(*BasketLocators.ITEMS)

    def is_empty_basket_message(self):
        self.is_element_present(*BasketLocators.EMPTY_BASKET_MESSAGE)