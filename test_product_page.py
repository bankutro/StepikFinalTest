from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest
import time

@pytest.mark.user_add_to_basket
class TestUserAddToBasketFromProductPage():
    @pytest.fixture
    def setup(self, browser):
        email_for_registration = str(time.time()) + "@fakemail.org"
        password_for_registration = "drowssap123123"

        product_page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/")
        product_page.open()
        product_page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.register_new_user(email_for_registration, password_for_registration)
        login_page.is_authorized_user()

    def test_user_cant_see_success_message(self, browser, setup):
        product_page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/")
        product_page.open()
        product_page.is_not_product_added_notification()

    @pytest.mark.need_review
    def test_user_add_product_to_basket(self, browser, setup):
        product_page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207")
        product_page.open()
        product_page.is_add_to_basket_button()
        product_page.add_to_basket()
        product_page.is_product_added_notification()
        product_page.correct_added_product_name()
        product_page.correct_added_product_price()
    

@pytest.mark.need_review
def test_guest_add_product_to_basket(browser):
    product_page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207")
    product_page.open()
    product_page.is_add_to_basket_button()
    product_page.add_to_basket()
    product_page.is_product_added_notification()
    product_page.correct_added_product_name()
    product_page.correct_added_product_price()

@pytest.mark.xfail(reason='Guest should see notifications after adding item to basket')
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/")
    product_page.open()
    product_page.add_to_basket()
    product_page.is_not_product_added_notification()

def test_guest_cant_see_success_message(browser):
    product_page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/")
    product_page.open()
    product_page.is_not_product_added_notification()

def test_message_disappeared_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/")
    product_page.open()
    product_page.is_notification_disappeared()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.is_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page (browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.is_add_to_basket_button()
    product_page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.is_basket_empty()
    basket_page.is_empty_basket_message()