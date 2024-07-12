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
    def test_handle_check_box(self, driver):
        method_name = sys._getframe().f_code.co_name
        driver.get(locators.test_check_box_sel_playground)

        # Commented once the tests are executed in non-headless mode
        driver.maximize_window()

        try:
            # Locating element by NAME
            elem_checkbox = locate_element(driver, By.CSS_SELECTOR, locators.cssSingleCheckBox)
            if elem_checkbox and elem_checkbox.is_enabled():
                elem_checkbox.click()
                driver.execute_script("lambda-status=passed")
        except NoSuchElementException:
            print(f"method_name: Checkbox not found")
            if exec_platform == 'cloud':
                driver.execute_script("lambda-status=failed")
            pytest.fail(f"{method_name}: Test Failed")

    def test_check_disabled_check_box(self, driver):
        method_name = sys._getframe().f_code.co_name

        driver.get(locators.test_check_box_sel_playground)

        # Commented once the tests are executed in non-headless mode
        driver.maximize_window()

        check_counter = 0
        try:
            for check_counter in range(4):
                result_xpath = locators.xDisabledCheckBox_1 + str(check_counter + 1) \
                    + locators.xDisabledCheckBox_2
                print(result_xpath)
                elem_checkbox = locate_element(driver, By.XPATH, result_xpath)
                # Check if the checkbox is enabled, it yes than click on it
                if elem_checkbox.is_enabled():
                    elem_checkbox.click()
                    print(f"{method_name}: Checkbox with xpath {result_xpath} is clicked")
                else:
                    print(f"{method_name}: \
                          Checkbox with xpath {result_xpath} is disabled, it is skipped")
        except NoSuchElementException:
            print(f"Fail: Checkbox not found")
            if exec_platform == 'cloud':
                driver.execute_script("lambda-status=failed")
            pytest.fail(f"{method_name}: Test Failed")