from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Basket items are presented, but should not be"

    def should_be_product_in_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Basket items are not presented"

    def should_be_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.IS_EMPTY_MESSAGE), \
            "Empty message is not presented"

    def should_not_be_empty_message(self):
        assert self.is_not_element_present(*BasketPageLocators.IS_EMPTY_MESSAGE), \
            "Empty message is presented"
