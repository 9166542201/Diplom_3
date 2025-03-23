import allure, urls

from pages.login_page import LoginPage


class TestLoginPage:
    @allure.title('переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_go_to_forgot_password_page(self, driver):
        login_page = LoginPage(driver).get(urls.LOGIN)
        login_page.go_to_forgot_password_page()
        assert login_page.verify_url(urls.FORGOT_PASSWORD)
