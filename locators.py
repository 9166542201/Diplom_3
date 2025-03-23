from selenium.webdriver.common.by import By


class Header:
    ACCOUNT = By.XPATH, "//a[@href='/account']"
    CONSTRUCTOR = By.XPATH, "(//a[@href='/'])[1]"
    FEED = By.XPATH, "//a[@href='/feed']"


class MainPage:
    MODAL_OPENED = By.CSS_SELECTOR, ".Modal_modal_opened__3ISw4"
    MODAL_CLOSE_BUTTON = By.CSS_SELECTOR, "button.Modal_modal__close__TnseK"
    INGREDIENT_1 = By.XPATH, "(//*[contains(@class, 'BurgerIngredient_ingredient__1TVf6')])[1]"
    INGREDIENT_3 = By.XPATH, "(//*[contains(@class, 'BurgerIngredient_ingredient__1TVf6')])[3]"
    INGREDIENT_3_counter = By.XPATH, ("(//*[contains(@class, 'BurgerIngredient_ingredient__1TVf6')])[3]"
                                      "//*[contains(@class, 'counter_counter__num__3nue1')]")
    LOADING_ANIMATION = By.CSS_SELECTOR, "[alt = 'loading animation']"
    BURGER_CONSTRUCTOR = By.CSS_SELECTOR, ".BurgerConstructor_basket__29Cd7"
    PLACE_ORDER_BUTTON = By.XPATH, "//*[text()='Оформить заказ']"
    ORDER_NUMBER = By.CSS_SELECTOR, ".Modal_modal__container__Wo2l_ h2"


class LoginPage:
    NAME = By.NAME, 'name'
    PASSWORD = By.CSS_SELECTOR, "[type='password']"
    LOGIN_BUTTON = By.CSS_SELECTOR, 'form button'
    FORGOT_PASSWORD = By.CSS_SELECTOR, "a[href='/forgot-password']"
    REGISTER = By.CSS_SELECTOR, "a[href='/register']"


class ForgotPasswordPage:
    NAME = By.NAME, 'name'
    RESET_BUTTON = By.CSS_SELECTOR, "form>button"


class ResetPasswordPage:
    PASSWORD = By.XPATH, "(//form//input)[1]"
    SVG_BUTTON = By.CSS_SELECTOR, "form svg"
    IS_ACTIVE = By.CSS_SELECTOR, "form .input_status_active"


class ProfilePage:
    NAME = By.CSS_SELECTOR, "input[name='name']"
    EXIT_BUTTON = By.XPATH, "//*[text()='Выход']"
    ORDER_HISTORY = By.XPATH, "//a[@href='/account/order-history']"


class OrderHistoryPage:
    ORDER_NUMBERS = By.CSS_SELECTOR, ".OrderHistory_textBox__3lgbs .text_type_digits-default"


class FeedPage:
    ORDER_NUMBERS = By.CSS_SELECTOR, ".OrderHistory_textBox__3lgbs .text_type_digits-default"
    ORDER_POPUP = By.CSS_SELECTOR, ".Modal_modal__container__Wo2l_ .text_type_digits-default"
    FOR_ALL_TIME_COUNTER = By.XPATH, "(//*[contains(@class, 'OrderFeed_number__2MbrQ')])[1]"
    FOR_TODAY_COUNTER = By.XPATH, "(//*[contains(@class, 'OrderFeed_number__2MbrQ')])[2]"
    ORDERS_IN_PROGRES = By.CSS_SELECTOR, 'ul.OrderFeed_orderListReady__1YFem li'
