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
class TestBitCoinClick:
    def test_bitcoin_selenium(self, driver):
        driver.get(locators.test_bitcoin_url)

        # Commented once the tests are executed in non-headless mode
        driver.maximize_window()

        action = ActionChains(driver)
        wait = WebDriverWait(driver, 5)

        try:
            element = driver.find_elements(By.PARTIAL_LINK_TEXT, "Participate")
            if (element):
                action.move_to_element(element[0]).perform()
                time.sleep(1)
            
            # Locate the menu with Buy Bitcoin
            elem_buy_item = driver.find_element(By.XPATH, \
                                "//ul[@id='menusimple']//a[.='Buy Bitcoin']")
            time.sleep(2)

            # Click on the menu item
            if (elem_buy_item):
                action.move_to_element(elem_buy_item).click().perform()

            # Wait for 10 seconds till the Document State is not complete
            wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')

            driver.switch_to.frame(1)

            # elem_dropdown = driver.find_element(By.CSS_SELECTOR,
            #                     "div:nth-child(1) > div > .rounded-foreground > .flex .text-callout")
            elem_dropdown = wait.until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, \
                                "div:nth-child(1) > div > .rounded-foreground > .flex .text-callout")))
            if (elem_dropdown):
                action.move_to_element(elem_dropdown).click().perform()

                try:
                    elem_search = wait.until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "[placeholder='Search']"))
                    )
                    elem_search.click()
                    elem_search.send_keys("ID")

                    # Click on the search result
                    driver.find_element(By.CSS_SELECTOR, ".ml-2").click()
                    # Switch back to the parent 
                    driver.switch_to.default_content()
                except Exception as e:
                    if exec_platform == 'cloud':
                        driver.execute_script("lambda-status=failed")
                    pytest.fail(f"Test failed: {str(e)}")
            time.sleep(2)
        except Exception as e:
            # Catch other exceptions
            print(f"Failed: Bitcoin demo, generic exception - {e}")
            if exec_platform == 'cloud':
                driver.execute_script("lambda-status=failed")