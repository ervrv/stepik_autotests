from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, "//*[text() = 'View basket']")


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FROM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner")


class BasketPageLocators:
    IS_EMPTY_MESSAGE = (By.XPATH, "//*[normalize-space(text()) = 'Your basket is empty.']")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket_items")
