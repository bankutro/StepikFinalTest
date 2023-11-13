from .base_page import BasePage
from .locators import ItemPageLocators

class ItemPage(BasePage):

    def is_add_to_basket_button(self):
        assert self.browser.find_element(*ItemPageLocators.ADD_TO_BASKET), "NO 'Add to Basket' button found"

    def add_to_basket(self):
        self.browser.find_element(*ItemPageLocators.ADD_TO_BASKET).click()
    
    def is_item_added_notification(self):
        assert self.is_element_present(*ItemPageLocators.ITEM_ADDED_NOTIFICATION), "There are NO notifications about added item"

    def is_not_item_added_notification(self):
        assert self.is_not_element_present(*ItemPageLocators.ITEM_ADDED_NOTIFICATION), "There ARE notifications about added item"

    def is_notification_disappeared(self):
        assert self.is_disappeared(*ItemPageLocators.ITEM_ADDED_NOTIFICATION), "Notification did NOT disappeared."

    def correct_added_item_name(self):
        notifications_about_added_item = self.browser.find_elements(*ItemPageLocators.ITEM_ADDED_NOTIFICATION)
        alert_item_name = notifications_about_added_item[0]
        print(alert_item_name.text)
        assert ItemPageLocators.ITEM_ADDED_NOTIFICATION_TEXT == alert_item_name.text, "Wrong item name in notification"

    def correct_added_item_price(self):
        notification_price = self.browser.find_elements(*ItemPageLocators.PRICE_NOTIFICATION)[0].text
        item_price = self.browser.find_element(*ItemPageLocators.ITEM_PRICE).text
        assert item_price in notification_price, "Item price does NOT equal to price in notification"

