import allure, locators
from base_page import BasePage


class OrderHistoryPage(BasePage):
    @allure.step('получаем все заказы из истории')
    def get_orders(self):
        return self.get_elements(locators.OrderHistoryPage.ORDER_NUMBERS)

    @allure.step('ждём появления заказов в истории')
    def wait_orders(self, number):
        self.wait_for_elements_appeared(locators.OrderHistoryPage.ORDER_NUMBERS, number)

    @allure.step('кликаем на Ленту заказов')
    def go_to_feed(self):
        self.click(locators.Header.FEED)
