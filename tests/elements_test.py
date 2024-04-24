import time

from pages.elements_page import TextBoxPage


class TestElements:
    class TestTextBox:
        def test(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_cur_addr, output_per_addr = text_box_page.check_filled_form()

            # Удаление префиксов
            if output_name.startswith("Name:"):
                output_name = output_name[len("Name:"):].strip()

            if output_email.startswith("Email:"):
                output_email = output_email[len("Email:"):].strip()

            if output_cur_addr.startswith("Current Address :"):
                output_cur_addr = output_cur_addr[len("Current Address :"):].strip()

            if output_per_addr.startswith("Permananet Address :"):
                output_per_addr = output_per_addr[len("Permananet Address :"):].strip()

            assert name == output_name, "the full name does not match"
            assert email == output_email, "the full email does not match"
            assert current_address == output_cur_addr, "the current_address does not match"
            assert permanent_address == output_per_addr, "the permanent_address does not match"


