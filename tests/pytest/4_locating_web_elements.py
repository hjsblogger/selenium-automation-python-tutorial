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

class TestLocatingElements:
    def test_locating_elements(self, driver):
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

            # Locating elements by TAG NAME
            elements_list = locate_elements(driver, By.TAG_NAME, locators.tagHeading)

            size_of_list = len(elements_list)
            print("Size of the element with tag h4:", size_of_list)

            print("Value of the first element with tag h4: " + elements_list[0].text)

            # Printing text of all the items in the list
            count = 0
            for element in elements_list:
                count += 1
                print("Value of the element " + str(count) + " with tag h4: " + element.text)

            # Locating elements by LINK TEXT
            driver.get(locators.test_sel_input_playground_url)
            elements_list = locate_elements(driver, By.LINK_TEXT, locators.linkPricing)
            if elements_list:
                elements_list[0].click()

            # Assert if the page title does not match the expected one
            try:
                page_title = driver.title
                assert locators.linkPricingTitle == page_title, f"Expected title '{locators.linkPricingTitle}' matches with'{page_title}'"
                print(f"Expected title '{locators.linkPricingTitle}' matches with'{page_title}'")
                if exec_platform == 'cloud':
                    driver.execute_script('lambda-status=passed')
            except AssertionError:
                if exec_platform == 'cloud':
                    driver.execute_script('lambda-status=failed')
                pytest.fail(f"Expected title '{locators.linkPricingTitle}'does not match with '{page_title}'")

            time.sleep(2)

            # Locating elements by PARTIAL LINK TEXT
            driver.get(locators.test_sel_playground_url)
            elements_list = locate_elements(driver, By.PARTIAL_LINK_TEXT, locators.linkPartialDown)

            # Printing text of all the items in the list
            count = 0
            for element in elements_list:
                count += 1
                print("Href element " + str(count) + " with tag h4: " \
                      + element.get_attribute('href'))

            if elements_list:
                elements_list[2].click()

            # Assert if the page title does not match the expected one
            try:
                element = locate_element(driver, By.CSS_SELECTOR, "#downloadButton")
                print(f"Pass: Page Title: '{driver.title}'")
                if exec_platform == 'cloud':
                    driver.execute_script('lambda-status=passed')
            except NoSuchElementException:
                if exec_platform == 'cloud':
                    driver.execute_script('lambda-status=failed')
                pytest.fail(f"Fail: Page Title: '{driver.title}'")

            time.sleep(2)    

        except Exception as e:
            # Catch other exceptions
            print(f"Failed: Locating web elements, generic exception - {e}")
            if exec_platform == 'cloud':
                driver.execute_script("lambda-status=failed")