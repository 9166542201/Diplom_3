import allure, locators
from base_page import BasePage


class ProfilePage(BasePage):

    @allure.step('кликаем История заказов')
    def go_to_order_history(self):
        self.click(locators.ProfilePage.ORDER_HISTORY)

    @allure.step('кликаем Выход')
    def exit_account(self):
        self.click(locators.ProfilePage.EXIT_BUTTON)

    @allure.step('кликаем Конструктор')
    def go_to_order_constructor(self):
        self.click(locators.Header.CONSTRUCTOR)
