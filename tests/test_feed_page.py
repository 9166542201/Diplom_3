import allure, urls
from pages.feed_page import FeedPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from pages.order_history_page import OrderHistoryPage


class TestFeedPage:

    @allure.title('если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_if_click_order_popup_with_order_details_will_open(self, driver, login):
        main_page = MainPage(driver)
        order_number = '#' + main_page.make_an_order()
        main_page.go_to_feed()
        main_page.url_to_be(urls.FEED)
        feed_page = FeedPage(driver)
        orders = [i for i in feed_page.get_orders_in_feed() if i.text == order_number]
        orders[0].click()
        assert feed_page.verify_that_order_modal_opened()
        assert feed_page.verify_popup_number(order_number)

    @allure.title('заказы из «Истории заказов» отображаются в «Ленте заказов»')
    def test_orders_from_history_displayed_on_order_feed(self, driver, login):
        main_page = MainPage(driver)
        main_page.make_an_order()
        main_page.make_an_order()
        main_page.go_to_account()
        main_page.url_to_be(urls.PROFILE)
        profile_page = ProfilePage(driver)
        profile_page.go_to_order_history()
        profile_page.url_to_be(urls.ORDER_HISTORY)
        order_history_page = OrderHistoryPage(driver)
        order_history_page.wait_orders(2)
        orders_from_history = [o.text for o in order_history_page.get_orders()]
        order_history_page.go_to_feed()
        order_history_page.url_to_be(urls.FEED)
        feed_page = FeedPage(driver)
        orders_from_feed = [o.text for o in feed_page.get_orders_in_feed()]
        assert feed_page.verify_orders_subset(orders_from_history, orders_from_feed)

    @allure.title('счётчик «Выполнено за всё время» увеличивается')
    def test_the_completed_for_all_time_counter_increases(self, driver, login):
        main_page = MainPage(driver)
        main_page.go_to_feed()
        main_page.url_to_be(urls.FEED)
        feed_page = FeedPage(driver)
        counter_before = feed_page.get_for_all_time_counter()
        feed_page.go_to_constructor()
        feed_page.url_to_be(urls.URL)
        main_page.make_an_order()
        main_page.go_to_feed()
        main_page.url_to_be(urls.FEED)
        counter_after = feed_page.get_for_all_time_counter()
        assert feed_page.verify_that_counter_increased(counter_before, counter_after)

    @allure.title('счётчик «Выполнено за сегодня» увеличивается')
    def test_the_completed_for_today_counter_increases(self, driver, login):
        main_page = MainPage(driver)
        main_page.go_to_feed()
        main_page.url_to_be(urls.FEED)
        feed_page = FeedPage(driver)
        counter_before = feed_page.get_for_today_counter()
        feed_page.go_to_constructor()
        feed_page.url_to_be(urls.URL)
        main_page.make_an_order()
        main_page.go_to_feed()
        main_page.url_to_be(urls.FEED)
        counter_after = feed_page.get_for_today_counter()
        assert feed_page.verify_that_counter_increased(counter_before, counter_after)

    @allure.title('номер заказа появляется в разделе В работе')
    def test_made_orders_is_in_progress_list(self, driver, login):
        main_page = MainPage(driver)
        order = main_page.make_an_order()
        main_page.go_to_feed()
        main_page.url_to_be(urls.FEED)
        feed_page = FeedPage(driver)
        assert feed_page.verify_that_order_in_progress_list(order)
