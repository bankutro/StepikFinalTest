from selenium.webdriver.common.by import By
from .pages.main_page import MainPage

def test_guest_can_go_to_login_page(browser):
    main_page = MainPage(browser, "http://selenium1py.pythonanywhere.com/")
    main_page.open()
    main_page.check_if_login_link()
    main_page.go_to_login_page()