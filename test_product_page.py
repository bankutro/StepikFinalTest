from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
from .pages.product_page import ProductPage
import pytest

@pytest.mark.skip
#@pytest.mark.parametrize("link", ["offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6", pytest.param("offer7", marks=pytest.mark.xfail), "offer8", "offer9"])
def test_product_add_to_basket(browser):
    product_page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207")
    product_page.open()
    product_page.is_add_to_basket_button()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.is_product_added_notification()
    product_page.correct_added_product_name()
    product_page.correct_added_product_price()
    
@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/")
    product_page.open()
    product_page.add_to_basket()
    product_page.is_not_product_added_notification()

@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    product_page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/")
    product_page.open()
    product_page.is_not_product_added_notification()

@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/")
    product_page.open()
    product_page.is_notification_disappeared()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.is_login_link()

def test_guest_can_go_to_login_page_from_product_page (browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_login_page()