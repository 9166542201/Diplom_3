import allure, locators
from base_page import BasePage


class ForgotPasswordPage(BasePage):

    @allure.step('кликаем на «Восстановить пароль»')
    def go_to_reset_password(self) -> None:
        self.send_keys(locators.ForgotPasswordPage.NAME, 'asdf')
        self.click(locators.ForgotPasswordPage.RESET_BUTTON)
