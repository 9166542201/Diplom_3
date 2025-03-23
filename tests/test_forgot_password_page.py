import allure, urls

from pages.forgot_password_page import ForgotPasswordPage


class TestForgotPasswordPage:
    @allure.title('ввод почты и клик по кнопке «Восстановить»')
    def test_go_to_reset_password(self, driver):
        forgot_password_page = ForgotPasswordPage(driver).get(urls.FORGOT_PASSWORD)
        forgot_password_page.go_to_reset_password()
        assert forgot_password_page.verify_url(urls.RESET_PASSWORD)
