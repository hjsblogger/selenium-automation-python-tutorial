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
    def test_scrap_ecommerce(self, driver):
        resultant_str = "Thanks for contacting us, we will get back to you shortly."

        driver.get(locators.test_sel_playground_url)

        # Commented once the tests are executed in non-headless mode
        driver.maximize_window()

        action = ActionChains(driver)
        wait = WebDriverWait(driver, 5)

        try:
            # Locating element by XPath
            element = locate_element(driver, By.XPATH, locators.xSubmitForm)
            element.click()

            # Locating element by CSS Selector
            element = locate_element(driver, By.CSS_SELECTOR, locators.cInpName)
            element.send_keys("Himanshu Sheth")

            # Locating element by ID
            element = locate_element(driver, By.ID, locators.idInputEmail)
            element.send_keys("testing@gmail.com")

            # Locating element by NAME
            element = locate_element(driver, By.NAME, locators.nameInputCompany)
            element.send_keys("LambdaTest")

            # Locating elements by CLASS NAME
            # document.getElementsByClassName("module-mz_product_listing")
            driver.get(locators.test_ecomm_playground_url)
            elements_list = locate_elements(driver, By.CLASS_NAME, locators.classProdListing)
            
            # This should return 5
            size_of_list = len(elements_list)
            print("Size of the product list:", size_of_list)

            driver.get(locators.test_sel_input_playground_url)


        except Exception as e:
            # Catch other exceptions
            print(f"Failed: Input Form Demo, generic exception - {e}")
            if exec_platform == 'cloud':
                driver.execute_script("lambda-status=failed")