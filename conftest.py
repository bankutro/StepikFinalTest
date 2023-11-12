import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en", help="Choose language (options: ru, en-gb, fr, it... so on / default: en)")
    parser.addoption('--browser', action='store', default="chrome", help="Choose browser: chrome or firefox")

@pytest.fixture(scope='function')
def browser(request):
    lang = request.config.getoption("language")
    b_name = request.config.getoption("browser")

    if b_name == "chrome" and lang != None:
        print("\nChrome starting...\n")
        options = Options()
        options.add_experimental_option('prefs',{'intl.accept_languages': lang})

        browser = webdriver.Chrome(options=options)
        browser.implicitly_wait(5)
    elif b_name == "firefox" and lang != None:
        print("Firefox starting...\n")
        f_profile = webdriver.FirefoxProfile()
        f_profile.set_preference('intl.accept_languages', lang)

        browser = webdriver.Firefox(firefox_profile=f_profile)
        browser.implicitly_wait(5)
    else:
        raise pytest.UsageError("--browser should be chrome or firefox")
    
    yield browser
    print("\nBrowser closing...\n")
    browser.quit()

@pytest.fixture(scope='function')
def lang(request):
    lang = request.config.getoption("language")
    return lang