from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.should_be_add_to_basket_button()
        btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        btn.click()

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BTN), \
            "No 'add-to-basket' button"

    def should_be_expected_product(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text.strip()
        assert self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text == \
               f"{product_name} has been added to your basket.", "Expected product was not added"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_not_be_success_message_left(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
