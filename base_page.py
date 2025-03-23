import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains

timeout = 1


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get(self, url):
        self.driver.get(url)
        return self

    def url_to_be(self, url):
        WebDriverWait(self.driver, timeout).until(expected_conditions.url_to_be(url))

    @allure.step('проверяем url')
    def verify_url(self, url):
        try:
            WebDriverWait(self.driver, timeout).until(expected_conditions.url_to_be(url))
        except TimeoutException:
            return False
        return True

    def is_element_visible(self, locator):
        try:
            WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))
        except TimeoutException:
            return False
        return True

    def is_element_invisible(self, locator):
        try:
            WebDriverWait(self.driver, 3).until(expected_conditions.invisibility_of_element(locator))
        except TimeoutException:
            return False
        return True

    def click(self, locator):
        element = WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator))
        element.click()
        return element

    def send_keys(self, locator, text):
        element = WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))
        element.send_keys(text)
        return element

    def get_elements(self, locator):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_all_elements_located(locator))

    def get_element(self, locator):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located(locator))

    def drag_and_drop(self, source, target):
        ActionChains(self.driver).drag_and_drop(self.get_element(source), self.get_element(target)).perform()

    def wait_for_elements_appeared(self, locator, number):
        WebDriverWait(self.driver, 9).until(lambda wd: len(wd.find_elements(*locator)) == number)

    def wait_for_string_is_in_list(self, string, locator):
        try:
            WebDriverWait(self.driver, 9).until(lambda wd: string in [e.text for e in wd.find_elements(*locator)])
        except TimeoutException:
            return False
        return True
