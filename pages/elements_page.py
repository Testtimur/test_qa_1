from locatars.elements_page_locators import TextBoxLocators
from pages.base_page import BasePage
import time


class TextBoxPage(BasePage):
    locators = TextBoxLocators()

    def fill_all_fields(self):
        self.element_is_visible(self.locators.FULL_NAME).send_keys('admin')
        self.element_is_visible(self.locators.EMAIL).send_keys('admin@gmail.com')
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys('admin95')
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys('admin94_2')
        self.element_is_visible(self.locators.SUBMIT).click()
        time.sleep(5)
