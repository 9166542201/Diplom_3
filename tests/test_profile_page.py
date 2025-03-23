import allure, urls

from pages.main_page import MainPage
from pages.profile_page import ProfilePage


class TestProfilePage:
    @allure.title('переход по клику на «Конструктор»')
    def test_go_to_constructor(self, driver, login):
        main_page = MainPage(driver)
        main_page.go_to_account()
        main_page.url_to_be(urls.PROFILE)
        profile_page = ProfilePage(driver)
        profile_page.go_to_order_constructor()
        assert profile_page.verify_url(urls.URL)

    @allure.title('переход в раздел «История заказов»')
    def test_go_order_history(self, driver, login):
        main_page = MainPage(driver)
        main_page.go_to_account()
        main_page.url_to_be(urls.PROFILE)
        profile_page = ProfilePage(driver)
        profile_page.go_to_order_history()
        assert profile_page.verify_url(urls.ORDER_HISTORY)

    @allure.title('проверяем выход из аккаунта')
    def test_exit_account(self, driver, login):
        main_page = MainPage(driver)
        main_page.go_to_account()
        main_page.url_to_be(urls.PROFILE)
        profile_page = ProfilePage(driver)
        profile_page.exit_account()
        assert profile_page.verify_url(urls.LOGIN)
