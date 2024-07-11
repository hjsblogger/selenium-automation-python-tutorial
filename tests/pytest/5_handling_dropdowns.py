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

class TestSeleniumPlayground:
    def test_handle_single_dropdown(self, driver):
        driver.get(locators.test_dropdown_sel_playground_url)

        # Commented once the tests are executed in non-headless mode
        driver.maximize_window()

        action = ActionChains(driver)
        wait = WebDriverWait(driver, 5)

        # Locating element by CSS Selector
        elem_dropdown = locate_element(driver, By.CSS_SELECTOR, locators.cssSingleSelect)
        if elem_dropdown:
            # Create a Select object
            select = Select(elem_dropdown)

            elem_dropdown.select_by_visible_text("Monday")
            print(f"The selected text is: '{elem_dropdown.text}'")

            # # Select options by visible text
            # select.select_by_visible_text('Option 1')
            # select.select_by_visible_text('Option 2')