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
    def test_handle_radio_button(self, driver):
        driver.get(locators.test_radio_button_sel_playground)

        # Commented once the tests are executed in non-headless mode
        driver.maximize_window()

        # Locating element by NAME
        elem_radio = locate_elements(driver, By.NAME, locators.nameRadioButton)
        if elem_radio and elem_radio[1].is_enabled():
            elem_radio[1].click()

            elem_button = locate_element(driver, By.CSS_SELECTOR, locators.cssGetValueButton)
            if elem_button:
                elem_button.click()
            # deselect methods are only available for multi-select drop-downs
                if "Female" in elem_button.text:
                    if exec_platform == 'cloud':
                        driver.execute_script("lambda-status=passed")
            if exec_platform == 'cloud':
                driver.execute_script("lambda-status=passed")
        else:
            if exec_platform == 'cloud':
                driver.execute_script("lambda-status=failed")
            pytest.fail(f"Test Failed")

    # Inspiration - https://www.lambdatest.com/blog/radio-buttons-in-selenium/
    def test_check_hidden_radio_buttons(self, driver):
        driver.get(locators.test_radio_button_hidden_playground)
        
        # Commented once the tests are executed in non-headless mode
        driver.maximize_window()
        
        # Explicit wait of 10 seconds
        wait = create_waits(driver, 10)

        # Wait for 10 seconds till the Document State is not complete
        wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')

        # Toggle the visibility of the hidden option
        toggle_button = locate_element(driver, By.ID, locators.idHiddenRadio)
        toggle_button.click()

        # Attempt to locate the radio button by ID and attempt to click it
        hidden_radio_button = locate_element(driver, By.ID, locators.idHiddenEnv)
        # Attempt to click the radio button
        hidden_radio_button.click()
    
        print(f"The radio button is displayed now.")

        if exec_platform == 'cloud':
            driver.execute_script("lambda-status=passed")
