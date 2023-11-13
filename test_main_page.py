from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
from .pages.locators import BasketLocators
from .pages.basket_page import BasketPage
import pytest

@pytest.mark.login_guest
class TestLoginFromMain():
    def test_guest_can_see_login_link(self, browser):
        main_page = MainPage(browser, "http://selenium1py.pythonanywhere.com/")
        main_page.open()
        main_page.is_login_link()

    def test_guest_can_go_to_login_page(self, browser):
        main_page = MainPage(browser, "http://selenium1py.pythonanywhere.com/")
        main_page.open()
        main_page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    main_page = MainPage(browser, "http://selenium1py.pythonanywhere.com/")
    main_page.open()
    main_page.is_view_basket_link()
    main_page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.is_basket_empty()
    basket_page.is_empty_basket_message()