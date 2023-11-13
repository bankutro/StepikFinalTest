from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
from .pages.item_page import ItemPage
import pytest
import time

@pytest.mark.skip
def test_guest_can_go_to_login_page(browser):
    main_page = MainPage(browser, "http://selenium1py.pythonanywhere.com/")
    main_page.open()
    main_page.check_if_login_link()
    main_page.go_to_login_page()

@pytest.mark.skip
@pytest.mark.parametrize("link", ["offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6", pytest.param("offer7", marks=pytest.mark.xfail), "offer8", "offer9"])
def test_product_add_to_basket(browser, link):
    item_page = ItemPage(browser, f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={link}")
    item_page.open()
    item_page.is_add_to_basket_button()
    item_page.add_to_basket()
    item_page.solve_quiz_and_get_code()
    item_page.is_item_added_notification()
    item_page.correct_added_item_name()
    item_page.correct_added_item_price()

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    item_page = ItemPage(browser, "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/")
    item_page.open()
    item_page.add_to_basket()
    item_page.is_not_item_added_notification()

def test_guest_cant_see_success_message(browser):
    item_page = ItemPage(browser, "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/")
    item_page.open()
    item_page.is_not_item_added_notification()

def test_message_disappeared_after_adding_product_to_basket(browser):
    item_page = ItemPage(browser, "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/")
    item_page.open()
    item_page.is_notification_disappeared()