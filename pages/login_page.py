import allure, locators
from base_page import BasePage


class LoginPage(BasePage):

    @allure.step('кликаем на «Восстановить пароль»')
    def go_to_forgot_password_page(self) -> None:
        self.click(locators.LoginPage.FORGOT_PASSWORD)

    @allure.step('авторизуемся')
    def fill_in_login_form_and_submit(self, user) -> None:
        login, password = user
        self.send_keys(locators.LoginPage.NAME, login)
        self.send_keys(locators.LoginPage.PASSWORD, password)
        self.click(locators.LoginPage.LOGIN_BUTTON)
