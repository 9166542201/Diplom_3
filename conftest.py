from selenium import webdriver
import pytest
import requests
import data
import urls
from pages.login_page import LoginPage


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--headless', action='store', default='N', help="Choose: Y or N")


@pytest.fixture
def driver(request):
    headless = True if request.config.getoption("headless").lower() == 'y' else False
    browser = request.config.getoption("browser").lower()
    match browser:
        case "chrome":
            options = webdriver.ChromeOptions()
            if headless: options.add_argument('--headless')
            options.add_argument("start-maximized")
            driver = webdriver.Chrome(options=options)
        case "firefox":
            options = webdriver.FirefoxOptions()
            if headless: options.add_argument("--headless")
            driver = webdriver.Firefox(options=options)
        case _:
            raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield driver
    driver.quit()


@pytest.fixture
def user():
    user = data.generate_user()
    response = requests.post(urls.REGISTER, json=user)
    json = response.json()
    if response.status_code != 200:
        raise RuntimeError("user creation failure")
    yield user['email'], user['password']
    requests.delete(urls.USER, headers={'authorization': json['accessToken']})


@pytest.fixture
def login(driver, user):
    login_page = LoginPage(driver).get(urls.LOGIN)
    login_page.fill_in_login_form_and_submit(user)
    login_page.url_to_be(urls.URL)
