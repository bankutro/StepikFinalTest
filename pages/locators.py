from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators():
    LOGIN_EMAIL_INPUT = (By.CSS_SELECTOR, '#id_login-username')
    LOGIN_PASSWORD_INPUT = (By.CSS_SELECTOR, '#id_login-password')

    REGISTRATION_EMAIL_INPUT = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTRATION_PASSWORD_INPUT = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTRATION_PASSWORD_REPEAT = (By.CSS_SELECTOR, '#id_registration-password2')

class ItemPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NOTIFICATIONS = (By.CSS_SELECTOR, "#messages")
    ITEM_ADDED_NOTIFICATION = (By.CSS_SELECTOR, "#messages .alertinner")
    ITEM_ADDED_NOTIFICATION_TEXT = 'Coders at Work has been added to your basket.'
    PRICE_NOTIFICATION = (By.CSS_SELECTOR, ".alertinner p")
    ITEM_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ITEM_PRICE = (By.CSS_SELECTOR, "p.price_color")