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
class TestSimpleSelenium:
    def test_simple_selenium(self, driver):
        resultant_str = "Thanks for contacting us, we will get back to you shortly."

        driver.get(locators.test_sel_playground_url)

        # Commented once the tests are executed in non-headless mode
        driver.maximize_window()

        action = ActionChains(driver)
        wait = WebDriverWait(driver, 5)

        try:
            element = driver.find_element(By.XPATH, locators.xSubmitForm)
            element.click()

            enter_details(driver, By.XPATH, locators.xInpName, "Testing", 2)

            enter_details(driver, By.XPATH, locators.xInpEmail, "testing@testing.com", 2)

            enter_details(driver, By.XPATH, locators.xInpPassword, "password", 2)

            enter_details(driver, By.CSS_SELECTOR, locators.cssCompany, "LambdaTest", 2)

            enter_details(driver, By.CSS_SELECTOR, locators.cWebName, "https://wwww.lambdatest.com", 2)

            country_dropdown = Select(driver.find_element(By.XPATH, locators.xInpCountry))
            country_dropdown.select_by_visible_text("United States")
            time.sleep(2)

            enter_details(driver, By.XPATH, locators.xInpCity, "San Jose", 2)

            enter_details(driver, By.CSS_SELECTOR, locators.cssAddress1, "Googleplex, 1600 Amphitheatre Pkwy", 2)

            enter_details(driver, By.CSS_SELECTOR, locators.cssAddress2, "Mountain View, CA 94043", 2)

            enter_details(driver, By.CSS_SELECTOR, locators.cssInpState, "California", 2)

            enter_details(driver, By.CSS_SELECTOR, locators.cssInpZip, "94088", 2)

            # Click on the Submit button
            submit_button = driver.find_element(By.CSS_SELECTOR, locators.cssInpButton)
            submit_button.click()
            time.sleep(2)
            # Assert if the page contains a certain text
            # try:
            #     assert "Thanks for contacting us, we will get back to you shortly" in driver.page_source
            #     driver.execute_script("lambda-status=passed")
            #     print("Passed: Input Form Demo")
            # except AssertionError:
            #     driver.execute_script("lambda-status=failed")
            #     print("Failed: Input Form Demo")

            # Option 2: Check if the text is within a specific element
            try:
                element = wait.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, ".success-msg"))
                )
                assert resultant_str in element.text, f"'{resultant_str}' not found in the specified element."
            except Exception as e:
                if exec_platform == 'cloud':
                    driver.execute_script("lambda-status=failed")
                pytest.fail(f"Text '{resultant_str}' not found: {str(e)}")
            
            time.sleep(5)
        except Exception as e:
            # Catch other exceptions
            print(f"Failed: Input Form Demo, generic exception - {e}")
            if exec_platform == 'cloud':
                driver.execute_script("lambda-status=failed")