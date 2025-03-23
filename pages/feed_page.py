import allure, locators
from selenium.webdriver.remote.webelement import WebElement
from base_page import BasePage


class FeedPage(BasePage):

    @allure.step('кликаем на Конструктор')
    def go_to_constructor(self) -> None:
        self.click(locators.Header.CONSTRUCTOR)

    @allure.step('получаем все заказы из Ленты')
    def get_orders_in_feed(self) -> list[WebElement]:
        return self.get_elements(locators.FeedPage.ORDER_NUMBERS)

    @allure.step('получаем все заказы В работе')
    def get_orders_in_progress(self) -> list[WebElement]:
        return self.get_elements(locators.FeedPage.ORDERS_IN_PROGRES)

    @allure.step('получаем «Выполнено за всё время»')
    def get_for_all_time_counter(self) -> int:
        return int(self.get_element(locators.FeedPage.FOR_ALL_TIME_COUNTER).text)

    @allure.step('получаем «Выполнено за сегодня»')
    def get_for_today_counter(self) -> int:
        return int(self.get_element(locators.FeedPage.FOR_TODAY_COUNTER).text)

    @allure.step('проверяем, что окно заказа открыто')
    def verify_that_order_modal_opened(self) -> bool:
        return self.is_element_visible(locators.FeedPage.ORDER_POPUP)

    @allure.step('проверяем номер заказа в окне заказа')
    def verify_popup_number(self, order_number) -> bool:
        popup_number = self.get_element(locators.FeedPage.ORDER_POPUP).text
        return popup_number == order_number

    @allure.step('проверяем, что номера из истории есть в ленте')
    def verify_orders_subset(self, orders_from_history, orders_from_feed) -> bool:
        return set(orders_from_history) <= set(orders_from_feed)

    @allure.step('проверяем, что счётчик увеличился')
    def verify_that_counter_increased(self, counter_before, counter_after) -> bool:
        return counter_after > counter_before

    @allure.step('проверяем, что заказ в списке «В работе»')
    def verify_that_order_in_progress_list(self, order) -> bool:
        return self.wait_for_string_is_in_list(order, locators.FeedPage.ORDERS_IN_PROGRES)
