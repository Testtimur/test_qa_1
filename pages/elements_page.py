import random

from selenium.webdriver.common.by import By

from generator.generator import generated_person
from locatars.elements_page_locators import TextBoxLocators, CheckBoxPageLocators
from pages.base_page import BasePage
import time


# Для удобства чтобы могли мы предать в return
# person_info = next() - он дает нам взять ровно одну итерацию (Full_name, email и т.п)


class TextBoxPage(BasePage):
    locators = TextBoxLocators()  #Создаю экземпляр класса и он будет включать в себя все атрибуты классы (FULL_NAME, EMAIL и т.п)

    # SELF это ссылка на сам объект (Еще раз глянуть)
    def fill_all_fields(self):
        person_info = next(generated_person())
        name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address

        self.element_is_visible(self.locators.FULL_NAME, timeout=1).send_keys(name)
        self.element_is_visible(self.locators.EMAIL, timeout=1).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS, timeout=1).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS, timeout=1).send_keys(permanent_address)
        self.element_is_visible(self.locators.SUBMIT, timeout=1).click()
        return name, email, current_address, permanent_address

    def check_filled_form(self):
        name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    def click_random_checkbox(self):
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        count = 21
        while count != 0:
            item = item_list[random.randint(1,15)] # Это метод случайно кликает от 1 до 15
            if count > 0:
                self.go_to_element(item)
                item.click()
                print(item)
                count -= 1
            else:
                break

    def get_checked_checkbox(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            title_item = box.find_element(By.XPATH, ".//ancestor::span[@class='rct-text']")
            data.append(title_item.text)
        return str(data).replace(' ', '').replace('.','').lower()

    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        return str(data).replace(' ', '').lower()
