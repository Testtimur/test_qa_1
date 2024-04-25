import time

from pages.elements_page import TextBoxPage, CheckBoxPage


class TestElements:
    class TestTextBox:
        def test_field_filling(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            name, email, current_address, permanent_address = text_box_page.fill_all_fields() #Тут он присвает
            output_name, output_email, output_cur_addr, output_per_addr = text_box_page.check_filled_form() #Тут мы функцию вызываем и он возвращает 4 значения

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



