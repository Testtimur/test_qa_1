import random
import requests
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from generator.generator import generated_person
from locatars.elements_page_locators import TextBoxLocators, CheckBoxPageLocators, RadioButtonPageLocators, \
    WebTablePageLocators, ButtonsPageLocators, LinksPageLocators
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
            item = item_list[random.randint(1, 15)]  # Это метод случайно кликает от 1 до 15
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
        return str(data).replace(' ', '').replace('.', '').lower()

    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        return str(data).replace(' ', '').lower().replace('doc', '').strip()


class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()

    def press_radio_button_yes(self):
        Yes = self.element_is_visible(self.locators.PRESS_RADIO_BUTTON_YES)
        Yes.click()
        return "Yes"

    def press_radio_button_impressive(self):
        impress = self.element_is_visible(self.locators.PRESS_RADIO_BUTTON_IMPRESSIVE)
        impress.click()
        return "Impressive"

    def check_radio_button(self):
        radio_button_test_result = self.element_is_visible(self.locators.OUTPUT_RESULT)
        return radio_button_test_result.text


class WebTablePage(BasePage):
    locators = WebTablePageLocators()

    def add_new_person(self):
        person_info = next(generated_person())
        first_name = person_info.first_name
        last_name = person_info.last_name
        email = person_info.email
        age = person_info.age
        salary = person_info.salary
        department = person_info.department

        self.element_is_visible(self.locators.ADD_BUTTON).click()
        self.element_is_visible(self.locators.FIRSTNAME_INPUT).send_keys(first_name)
        self.element_is_visible(self.locators.LASTNAME_INPUT).send_keys(last_name)
        self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
        self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
        self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
        self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)
        self.element_is_visible(self.locators.SUBMIT).click()
        return [first_name, last_name, str(age), email, str(salary), department]

    def check_add_person(self):
        person_list = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        data = []
        for person in person_list:
            data.append(person.text.splitlines())
        return data

    def search_person(self, key_word):
        self.element_is_present(self.locators.WORD_INPUT).send_keys(key_word)

    def check_search_person(self):
        delete_button = self.element_is_present(self.locators.DELETE_BUTTON)
        row = delete_button.find_element("xpath", "//div[@class='rt-tr-group']")
        return row.text.splitlines()

    def edit_person(self):
        person_info = next(generated_person())
        age = person_info.age
        self.element_is_visible(self.locators.EDIT_PERSON).click()
        age_input = self.element_is_visible(self.locators.AGE_INPUT)
        age_input.clear()
        age_input.send_keys(age)
        self.element_is_visible(self.locators.SUBMIT).click()
        return str(age)

    def delete_person(self):
        delete_button = self.element_is_present(self.locators.DELETE_BUTTON)
        delete_button.click()

    def check_delete_person(self):
        delete_person = self.element_is_present(self.locators.DELETE_PERSON)
        return delete_person.text

class ButtonsPage(BasePage):

    locators = ButtonsPageLocators()

    def click_on_different_button(self, type_click):
        if type_click == "double":
            self.action_double_click(self.element_is_visible(self.locators.DOUBLE_BUTTON))
            return self.check_clicked_on_the_button(self.locators.SUCCESS_DOUBLE)
        if type_click == "click":
            click_button = self.element_is_visible(self.locators.CLICK_ME_BUTTON)
            click_button.click()
            return self.check_clicked_on_the_button(self.locators.SUCCESS_CLICK_ME)

    def check_clicked_on_the_button(self, element):
        return self.element_is_present(element).text

class LinksPage(BasePage):
    locatars = LinksPageLocators()

    def check_new_tab_link(self,):
        simple_link = self.element_is_visible(self.locatars.SIMPLE_LINK)
        link_href = simple_link.get_attribute("href")
        request = requests.get(link_href)
        if request.status_code == 200:
            simple_link.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            url = self.driver.current_url
            return link_href, url
        else:
            return request.status_code

    def check_broken_link(self,url):
        request = requests.get(url)
        if request.status_code == 200:
            self.element_is_present(self.locatars.BAD_REQUEST).click()
        else:
            return request.status_code










