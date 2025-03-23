import allure, urls

from pages.main_page import MainPage


class TestMainPage:
    @allure.title('переход по клику на «Личный кабинет» на страницу Логина')
    def test_go_to_login_page(self, driver):
        main_page = MainPage(driver).get(urls.URL)
        main_page.go_to_account()
        assert main_page.verify_url(urls.LOGIN)

    @allure.title('переход по клику на «Личный кабинет» на Профиль')
    def test_go_to_profile_page(self, driver, login):
        main_page = MainPage(driver)
        main_page.go_to_account()
        assert main_page.verify_url(urls.PROFILE)

    @allure.title('переход по клику на «Лента заказов»')
    def test_go_to_feed(self, driver):
        main_page = MainPage(driver).get(urls.URL)
        main_page.go_to_feed()
        assert main_page.verify_url(urls.FEED)

    @allure.title('проверяем всплывающее окно ингредиента')
    def test_select_ingredients(self, driver):
        main_page = MainPage(driver).get(urls.URL)
        main_page.select_ingredient()
        assert main_page.verify_that_ingredient_modal_opened()
        main_page.close_ingredient()
        assert main_page.verify_that_ingredient_modal_closed()

    @allure.title('при добавлении ингредиента в заказ, увеличивается счётчик данного ингредиента')
    def test_add_ingredient_to_constructor(self, driver):
        main_page = MainPage(driver).get(urls.URL)
        main_page.add_ingredient_to_constructor()
        counter = main_page.add_ingredient_to_constructor()
        assert main_page.verify_counter(counter, 2)

    @allure.title('авторизованный пользователь может оформить заказ')
    def test_make_an_order(self, driver, login):
        main_page = MainPage(driver)
        order_number = main_page.make_an_order()
        assert main_page.verify_order_number(order_number)
