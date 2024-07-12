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
    def test_handle_js_alerts1(self, driver):
        method_name = sys._getframe().f_code.co_name
        driver.get(locators.test_alerts_sel_playground)

        # Commented once the tests are executed in non-headless mode
        driver.maximize_window()

        try:
            # Locating element by NAME
            elem_button = locate_element(driver, By.CSS_SELECTOR, locators.cssAlert_1)
            if elem_button:
                elem_button.click()

            # Switch to the alert
            alert = driver.switch_to.alert

            # Sleep added only for demo, else it is a very bad practice!    
            time.sleep(2)

            # Accept Alert
            alert.accept()

            # Sleep added only for demo, else it is a very bad practice!    
            time.sleep(2)
        except NoSuchElementException:
            print(f"method_name: test failed")
            if exec_platform == 'cloud':
                driver.execute_script("lambda-status=failed")
            pytest.fail(f"{method_name}: Test Failed")

    def test_handle_js_alerts2(self, driver):
        method_name = sys._getframe().f_code.co_name
        driver.get(locators.test_alerts_sel_playground)

        wait = WebDriverWait(driver, 5)

        # Commented once the tests are executed in non-headless mode
        driver.maximize_window()

        try:
            # Locating element by NAME
            elem_button = locate_element(driver, By.CSS_SELECTOR, locators.cssAlert_2)
            if elem_button:
               elem_button.click()

		    # Wait for the alert to be present
            alert = wait.until(EC.alert_is_present())

            # Switch to the alert
            alert = driver.switch_to.alert

            # Sleep added only for demo, else it is a very bad practice!    
            time.sleep(4)

            # Dismiss the Alert
            alert.dismiss()

            # Sleep added only for demo, else it is a very bad practice!    
            time.sleep(4)

            # Wait for the modal box to be visible
            elem_demo = wait.until(EC.presence_of_element_located((By.XPATH, \
                        "//p[@id='confirm-demo']")))

            # Check if the dismiss was done
            if elem_demo:
                print(f"{method_name}: Final output string is: {elem_demo.text}")
        except NoSuchElementException:
            print(f"{method_name}: test failed")
            if exec_platform == 'cloud':
                driver.execute_script("lambda-status=failed")
            pytest.fail(f"{method_name}: Test Failed")

    def test_handle_js_alerts3(self, driver):
        method_name = sys._getframe().f_code.co_name
        driver.get(locators.test_alerts_sel_playground)
        

        # Commented once the tests are executed in non-headless mode
        driver.maximize_window()

        wait = WebDriverWait(driver, 5)

        try:
            # Locating element by NAME
            elem_button = locate_element(driver, By.CSS_SELECTOR, locators.cssAlert_3)
            if elem_button:
               elem_button.click()

            # Wait for the alert to be present
            alert = wait.until(EC.alert_is_present())
            
            # Switch to the alert
            alert = driver.switch_to.alert

            # Sleep added only for demo, else it is a very bad practice!    
            time.sleep(2)

            # Enter content in the text box
            alert.send_keys("LambdaTest is an awesome platform")

            time.sleep(2)

            # Accept the Alert
            alert.accept()

            # Sleep added only for demo, else it is a very bad practice!    
            time.sleep(2)
            
            # Wait for the modal box to be visible
            elem_prompt_demo = wait.until(EC.presence_of_element_located((By.XPATH, \
                                "//p[@id='prompt-demo']")))
            print(f"{method_name}: Final output string is: {elem_prompt_demo.text}")
        except NoSuchElementException:
            print(f"{method_name}: test failed")
            if exec_platform == 'cloud':
                driver.execute_script("lambda-status=failed")
            pytest.fail(f"{method_name}: Test Failed")