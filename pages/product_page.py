from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def is_add_to_basket_button(self):
        assert self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET), "NO 'Add to Basket' button found"

    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()
    
    def is_product_added_notification(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_ADDED_NOTIFICATION), "There are NO notifications about added Product"

    def is_not_product_added_notification(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_ADDED_NOTIFICATION), "There ARE notifications about added Product"

    def is_notification_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_ADDED_NOTIFICATION), "Notification did NOT disappeared."

    def correct_added_product_name(self):
        notifications_about_added_product = self.browser.find_elements(*ProductPageLocators.PRODUCT_ADDED_NOTIFICATION)
        alert_product_name = notifications_about_added_product[0]
        assert ProductPageLocators.PRODUCT_ADDED_NOTIFICATION_TEXT == alert_product_name.text, "Wrong text in notification"

    def correct_added_product_price(self):
        notification_price = self.browser.find_elements(*ProductPageLocators.PRICE_NOTIFICATION)[0].text
        Product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert Product_price in notification_price, "Product price does NOT equal to price in notification"

