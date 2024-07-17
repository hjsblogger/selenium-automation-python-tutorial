# Import the locators file
import sys
import os
sys.path.append(sys.path[0] + "/../..")
from pageobject.locators import locators
from pageobject.locators import *

from pageobject.helpers import helpers
from pageobject.helpers import *

exec_platform = os.getenv('EXEC_PLATFORM')

@pytest.mark.usefixtures('driver')

class TestHandlingDropdowns:
    def test_handle_single_dropdown(self, driver):
        driver.get(locators.test_dropdown_sel_playground_url)

        # Commented once the tests are executed in non-headless mode
        driver.maximize_window()

        # Locating element by CSS Selector
        elem_dropdown = locate_element(driver, By.CSS_SELECTOR, locators.cssSingleSelect)
        if elem_dropdown:
            # Create a Select object
            select_dropdown = Select(elem_dropdown)

            # def select_by_visible_text(self, text: str) -> None:
            select_dropdown.select_by_visible_text("Monday")
            print(f"Visible Text: The selected text is: '{select_dropdown.first_selected_option.text}'")

            # def select_by_index(self, index: int) -> None:
            select_dropdown.select_by_index(4)
            print(f"Index: The selected text is: '{select_dropdown.first_selected_option.text}'")

            # def select_by_value(self, value: str) -> None:
            select_dropdown.select_by_value('Friday')
            print(f"Value: The selected text is: '{select_dropdown.first_selected_option.text}'")

            # deselect methods are only available for multi-select drop-downs
            driver.execute_script("lambda-status=passed")
        else:
            if exec_platform == 'cloud':
                driver.execute_script("lambda-status=failed")
            pytest.fail(f"Test Failed")

    def test_handle_multiselect_dropdown(self, driver):
        driver.get(locators.test_dropdown_sel_playground_url)

        # Commented once the tests are executed in non-headless mode
        driver.maximize_window()

        # Locating element by CSS Selector
        elem_dropdown = locate_element(driver, By.ID, locators.idMultiSelect)
        if elem_dropdown:
            # Create a Select object
            select_dropdown = Select(elem_dropdown)

            # def select_by_visible_text(self, text: str) -> None:
            dropdown_select_element(select_dropdown, "visible_text", "Florida")
            dropdown_select_element(select_dropdown, "visible_text", "Ohio")
            dropdown_select_element(select_dropdown, "visible_text", "Texas")

            time.sleep(5)

            print_select_element(select_dropdown, "Visible Text")

            # def select_by_index(self, index: int) -> None:
            dropdown_select_element(select_dropdown, "select_index", 4)
            dropdown_select_element(select_dropdown, "select_index", 2)
            dropdown_select_element(select_dropdown, "select_index", 5)

            time.sleep(5)

            print_select_element(select_dropdown, "Index")

            # def select_by_value(self, value: str) -> None:
            dropdown_select_element(select_dropdown, "select_value", 'Washington')
            dropdown_select_element(select_dropdown, "select_value", 'New York')

            time.sleep(5)

            print_select_element(select_dropdown, "Value")

            # deselect methods are only available for multi-select drop-downs
            if exec_platform == 'cloud':
                driver.execute_script("lambda-status=passed")
        else:
            if exec_platform == 'cloud':
                driver.execute_script("lambda-status=failed")
            pytest.fail(f"Test Failed")