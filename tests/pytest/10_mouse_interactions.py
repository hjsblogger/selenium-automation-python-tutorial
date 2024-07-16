# Import the locators file
import sys
import os
sys.path.append(sys.path[0] + "/../..")
from pageobject.locators import locators
from pageobject.locators import *

from pageobject.helpers import helpers
from pageobject.helpers import *
from selenium.webdriver.common.keys import Keys

exec_platform = os.getenv('EXEC_PLATFORM')

@pytest.mark.usefixtures('driver')
class TestSeleniumPlayground:
    # Reference - https://www.selenium.dev/documentation/webdriver/
    # actions_api/mouse/#drag-and-drop-on-element
    def test_drag_drop_element(self, driver):
        method_name = sys._getframe().f_code.co_name
        driver.get(locators.test_mouse_sel_playground)

        # Commented once the tests are executed in non-headless mode
        driver.maximize_window()

        action = create_actions(driver)

        try:
            # Locating the draggable & droppable using the appropriate property
            elem_draggable_1 = locate_element(driver, By.XPATH, locators.xDraggableFrame_1)
            elem_draggable_2 = locate_element(driver, By.XPATH, locators.xDraggableFrame_2)
            elem_droppable = locate_element(driver, By.XPATH, locators.xDroppableFrame)

            if elem_draggable_1 and elem_draggable_2:
                action.drag_and_drop(elem_draggable_1, elem_droppable) \
                    .perform()
                
                # Sleep added only for demo, else it is a very bad practice!    
                time.sleep(2)

                action.drag_and_drop(elem_draggable_2, elem_droppable) \
                    .perform()
                
                # Sleep added only for demo, else it is a very bad practice!    
                time.sleep(2)

                # Check if both the items were dropped
                elem_dropped_list = locate_element(driver, By.ID, locators.idDroppableList)

                # Locate all span elements within this div
                elem_span = locate_elements_gen(elem_dropped_list,
                                    By.TAG_NAME, "span")

                # Extract and print the text from each span element
                str_1 = "Draggable 1"
                str_2 = "Draggable 2"

                for span in elem_span:
                    if  (span.text.lower() == str_1.lower()) or \
                        (span.text.lower() == str_2.lower()):
                            print(f"Draggable Text: {span.text}")
                    else:
                        if exec_platform == 'cloud':
                            driver.execute_script("lambda-status=failed")
                        pytest.fail(f"{method_name}: Test Failed")
        except NoSuchElementException:
            print(f"method_name: test failed")
            if exec_platform == 'cloud':
                driver.execute_script("lambda-status=failed")
            pytest.fail(f"{method_name}: Test Failed")
    
    # Reference - https://www.selenium.dev/documentation/webdriver/
    # actions_api/mouse/#move-to-element
    def test_move_to_element(self, driver):
        method_name = sys._getframe().f_code.co_name
        driver.get(locators.test_ecomm_playground_url)

        # Commented once the tests are executed in non-headless mode
        driver.maximize_window()

        action = create_actions(driver)
        wait = create_waits(driver, 2)

        try:
            # Locate the menu with text Addons
            elem_menu_item = locate_element(driver, By.PARTIAL_LINK_TEXT, \
                                locators.linkFeaturedItems)
            if (elem_menu_item):
                action.move_to_element(elem_menu_item).perform()
                time.sleep(1)
            
            # Locate the menu with text Designs
            elem_design_item = locate_element(driver, By.PARTIAL_LINK_TEXT, \
                                locators.linkDesignItems)
            # print(elem_design_item)

            time.sleep(2)

            # Click on the menu item
            if (elem_design_item):
                action.move_to_element(elem_design_item).click().perform()

                        # print(elem_design_item)

            time.sleep(2)

            current_url = driver.current_url
            print(f"The current URL is: {current_url}")
            # Assert that the URL does not match the expected URL
            assert current_url == locators.targetURL, \
                        f"URL matches the expected URL: {locators.targetURL}"

            try:
                element = wait.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "[data-id='214968'] > .mb-4"))
                )
                assert locators.resultant_str in element.text, \
                    f"'{locators.resultant_str}' not found in the specified element."
            except Exception as e:
                if exec_platform == 'cloud':
                    driver.execute_script("lambda-status=failed")
                pytest.fail(f"Text '{locators.resultant_str}' not found: {str(e)}")
            
            if exec_platform == 'cloud':
                  driver.execute_script("lambda-status=passed")
        except NoSuchElementException:
            print(f"method_name: test failed")
            if exec_platform == 'cloud':
                driver.execute_script("lambda-status=failed")
            pytest.fail(f"{method_name}: Test Failed")