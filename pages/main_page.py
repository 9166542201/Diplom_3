import allure, locators

from base_page import BasePage


class MainPage(BasePage):

    @allure.step('кликаем на Личный кабинет')
    def go_to_account(self) -> None:
        self.click(locators.Header.ACCOUNT)

    @allure.step('кликаем на Конструктор')
    def go_to_constructor(self) -> None:
        self.click(locators.Header.CONSTRUCTOR)

    @allure.step('кликаем на Ленту заказов')
    def go_to_feed(self) -> None:
        self.click(locators.Header.FEED)

    @allure.step('кликаем на ингредиент')
    def select_ingredient(self) -> None:
        self.click(locators.MainPage.INGREDIENT_1)

    @allure.step('проверяем, что окно ингредиента открыто')
    def verify_that_ingredient_modal_opened(self) -> bool:
        return self.is_element_visible(locators.MainPage.MODAL_OPENED)

    @allure.step('зарыть окно ингредиента')
    def close_ingredient(self) -> None:
        self.click(locators.MainPage.MODAL_CLOSE_BUTTON)

    @allure.step('проверяем, что окно ингредиента закрыто')
    def verify_that_ingredient_modal_closed(self) -> bool:
        return self.is_element_invisible(locators.MainPage.MODAL_OPENED)

    @allure.step('добавляем ингредиент в заказ')
    def add_ingredient_to_constructor(self) -> int:
        self.drag_and_drop(locators.MainPage.INGREDIENT_3, locators.MainPage.BURGER_CONSTRUCTOR)
        return int(self.get_element(locators.MainPage.INGREDIENT_3_counter).text)

    @allure.step('проверяем счётчик ингредиента ')
    def verify_counter(self, counter, number) -> bool:
        return counter == number

    @allure.step('делаем заказ')
    def make_an_order(self) -> str:
        self.drag_and_drop(locators.MainPage.INGREDIENT_1, locators.MainPage.BURGER_CONSTRUCTOR)
        self.drag_and_drop(locators.MainPage.INGREDIENT_3, locators.MainPage.BURGER_CONSTRUCTOR)
        self.click(locators.MainPage.PLACE_ORDER_BUTTON)
        self.is_element_invisible(locators.MainPage.LOADING_ANIMATION)
        order_number = '0' + self.get_element(locators.MainPage.ORDER_NUMBER).text
        self.click(locators.MainPage.MODAL_CLOSE_BUTTON)
        self.is_element_invisible(locators.MainPage.ORDER_NUMBER)
        return order_number

    @allure.step('проверяем, что вернулся непустой номер заказа')
    def verify_order_number(self, order_number) -> bool:
        return type(order_number) is str and len(order_number) > 0
