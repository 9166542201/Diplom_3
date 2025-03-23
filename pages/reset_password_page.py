import allure, locators
from base_page import BasePage


class ResetPasswordPage(BasePage):

    @allure.step('кликаем на «Показать пароль»')
    def show_password(self):
        self.click(locators.ResetPasswordPage.SVG_BUTTON)

    @allure.step('проверяем, что поле пароля подсвечено')
    def verify_that_password_field_highlighted(self) -> bool:
        return self.is_element_visible(locators.ResetPasswordPage.IS_ACTIVE)
