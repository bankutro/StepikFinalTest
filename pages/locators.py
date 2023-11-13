from selenium.webdriver.common.by import By

class LoginPageLocators():
    LOGIN_EMAIL_INPUT = (By.CSS_SELECTOR, '#id_login-username')
    LOGIN_PASSWORD_INPUT = (By.CSS_SELECTOR, '#id_login-password')

    REGISTRATION_EMAIL_INPUT = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTRATION_PASSWORD_INPUT = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTRATION_PASSWORD_REPEAT = (By.CSS_SELECTOR, '#id_registration-password2')

    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "button[value='Register']")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_ADDED_NOTIFICATION = (By.CSS_SELECTOR, "#messages .alertinner")
    PRODUCT_ADDED_NOTIFICATION_TEXT = 'Coders at Work has been added to your basket.'
    PRICE_NOTIFICATION = (By.CSS_SELECTOR, ".alertinner p")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inv")
    BASKET_LINK = (By.XPATH, "//a[contains(text(), 'View basket')]")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketLocators():
    ITEMS = (By.CSS_SELECTOR, ".basket_items")
    EMPTY_BASKET_MESSAGE = (By.XPATH, "//p[contains(text(), 'Your basket is empty.')]")