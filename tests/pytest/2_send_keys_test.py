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

class TestSendKeysDemo:
    def test_send_keys_demo(self, driver):
        driver.get(locators.test_ecomm_login_playground_url)

        # Commented once the tests are executed in non-headless mode
        driver.maximize_window()

        action = ActionChains(driver)
        wait = WebDriverWait(driver, 5)

        try:
            element = locate_element(driver, By.CSS_SELECTOR, locators.cssLoginEmail)
            element.send_keys(locators.loginEmail)

            time.sleep(4)
            element.clear()

            # Delay is added to check whether the field was cleared or not
            time.sleep(5)
            element.send_keys(locators.loginEmail)

            element = locate_element(driver, By.XPATH, locators.xLoginPass)
            element.send_keys(locators.loginPassword)

            # Click on the Submit button
            submit_button = driver.find_element(By.CSS_SELECTOR, locators.cssLoginButton)
            submit_button.click()

            # Not a good practice to use blocking waits, but used for demo purpose
            time.sleep(2)
            # Assert if the page title does not match the expected one
            try:
                page_title = driver.title
                assert locators.strPageTitle == page_title, f"Expected title '{locators.strPageTitle}' matches with'{page_title}'"
                if exec_platform == 'cloud':
                    driver.execute_script('lambda-status=passed')
            except AssertionError:
                if exec_platform == 'cloud':
                    driver.execute_script('lambda-status=failed')
                pytest.fail(f"Expected title '{locators.strPageTitle}'does not match with '{page_title}'")

            time.sleep(2)

        except Exception as e:
            # Catch other exceptions
            print(f"Failed: Input Form Demo, generic exception - {e}")
            if exec_platform == 'cloud':
                driver.execute_script("lambda-status=failed")