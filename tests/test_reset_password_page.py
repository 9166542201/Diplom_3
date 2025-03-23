import allure, urls

from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage


class TestResetPasswordPage:
    @allure.title('клик по кнопке показать пароль подсвечивает его')
    def test_password_field_is_active(self, driver):
        forgot_password_page = ForgotPasswordPage(driver).get(urls.FORGOT_PASSWORD)
        forgot_password_page.go_to_reset_password()
        forgot_password_page.url_to_be(urls.RESET_PASSWORD)
        reset_password_page = ResetPasswordPage(driver)
        reset_password_page.show_password()
        assert reset_password_page.verify_that_password_field_highlighted()
