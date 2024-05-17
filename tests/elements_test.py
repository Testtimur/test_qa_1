import time

from pages.base_page import BasePage
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage


class TestElements:
    class TestTextBox:
        def test_field_filling(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            name, email, current_address, permanent_address = text_box_page.fill_all_fields()  #Тут он присвает
            output_name, output_email, output_cur_addr, output_per_addr = text_box_page.check_filled_form()  #Тут мы функцию вызываем и он возвращает 4 значения

            assert name == output_name, "the full name does not match"
            assert email == output_email, "the full email does not match"
            assert current_address == output_cur_addr, "the current_address does not match"
            assert permanent_address == output_per_addr, "the permanent_address does not match"

    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkbox()
            output_result = check_box_page.get_output_result()
            assert input_checkbox == output_result, "the input checkbox does not match"

    class TestRadioButton:
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.press_radio_button_yes()
            radio_button_page.check_radio_button()
            otp_result = radio_button_page.check_radio_button()
            yes = radio_button_page.press_radio_button_yes()
            assert yes == otp_result

        def test_radio_button_impressive(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.press_radio_button_impressive()
            radio_button_page.check_radio_button()
            otp_result = radio_button_page.check_radio_button()
            impressive = radio_button_page.press_radio_button_impressive()
            assert impressive == otp_result

    class TestWebTable:

        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            check_person_table = web_table_page.check_add_person()
            assert new_person in check_person_table

        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            key_word = web_table_page.add_new_person()[0]
            web_table_page.search_person(key_word)
            table_result = web_table_page.check_search_person()
            assert key_word in table_result

        def test_web_table_edit_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            lastname = web_table_page.add_new_person()[1]
            web_table_page.search_person(lastname)
            age = web_table_page.edit_person()
            check_person_table = web_table_page.check_search_person()
            assert age in check_person_table

        def test_web_table_delete_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            lastname = web_table_page.add_new_person()[1]
            web_table_page.search_person(lastname)
            web_table_page.delete_person()
            check_delete_person = web_table_page.check_delete_person()
            assert check_delete_person == 'No rows found'

class TestButtonPage:

     def test_different_click_on_the_buttons(self, driver):
        button_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
        button_page.open()
        double = button_page.click_on_different_button('double')
        click = button_page.click_on_different_button('click')
        assert double == "You have done a double click"
        assert click == "You have done a dynamic click"



