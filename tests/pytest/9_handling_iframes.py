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
    def test_handle_nested_frame(self, driver):
        method_name = sys._getframe().f_code.co_name
        driver.get(locators.test_nested_frame_sel_playground)

        # Commented once the tests are executed in non-headless mode
        driver.maximize_window()

        try:
            # Locating the top frame using the NAME property
            elem_frame = locate_element(driver, By.NAME, locators.nameFrameTop)
            if elem_frame:
                driver.switch_to.frame(elem_frame)
                elem_body = locate_element(driver, By.XPATH, "//p[.='Top']")
                if (elem_body):
                    # There is no other operation possible with this frame
                    elem_body.click()

            # Sleep added only for demo, else it is a very bad practice!    
            time.sleep(2)

            # Switching to iFrame using index property
            # Since frames on the test page do not have id property,
            # we won't be demoing this method in the tutorial
            # driver.switch_to.frame(frame_index)

            # Switch back to the main window
            driver.switch_to.default_content()
        except NoSuchElementException:
            print(f"method_name: test failed")
            if exec_platform == 'cloud':
                driver.execute_script("lambda-status=failed")
            pytest.fail(f"{method_name}: Test Failed")

    # Earlier used in https://github.com/hjsblogger/web-automation-with-pyppeteer/blob/main/
    # tests/handling-iframe/test_page_class_iframe.py
    def test_handle_iframe(self, driver):
        action = ActionChains(driver)
        wait = WebDriverWait(driver, 5)

        method_name = sys._getframe().f_code.co_name
        driver.get(locators.test_iframe_sel_playground)

        # Commented once the tests are executed in non-headless mode
        driver.maximize_window()

        try:
            # Locating the frame using the ID property
            elem_frame = locate_element(driver, By.ID, locators.idFrame)
            if elem_frame:
                driver.switch_to.frame(elem_frame)
                elem_body = locate_element(driver, By.CSS_SELECTOR, locators.classBody)
                if (elem_body):
                    # Get inside the frame
                    elem_body.click()

                    time.sleep(2)

                    # https://github.com/hjsblogger/web-automation-with-pyppeteer/blob/
                    # main/tests/handling-iframe/test_page_class_iframe.py#L64
                    action.click(elem_body).click(elem_body).click(elem_body).perform()

                    # https://github.com/hjsblogger/web-automation-with-pyppeteer/blob/main/
                    # tests/handling-iframe/test_page_class_iframe.py#L65
                    elem_body.send_keys(Keys.BACKSPACE)

                    # Type the test message
                    str_message = "LambdaTest is an awesome platform!"
                    elem_body.send_keys(str_message)

                    time.sleep(2)

                    # https://github.com/hjsblogger/web-automation-with-pyppeteer/blob/
                    # main/tests/handling-iframe/test_page_class_iframe.py#L72
                    action.click(elem_body).click(elem_body).click(elem_body).perform()

                    # Wait for 2 seconds
                    time.sleep(2)

                    # Find the underline button using XPath and wait until it is clickable
                    underline_button = wait.until(
                            EC.element_to_be_clickable((By.XPATH,  \
                                    locators.xloc_bold_button))
                    )

                    # Find the bold button using CSS selector
                    bold_button = driver.find_element(By.XPATH, \
                                    locators.xloc_underline_button)

                    time.sleep(1)

                    # Click on the underline button
                    underline_button.click()
                    time.sleep(1)

                    # Click on the bold button
                    bold_button.click()
                    time.sleep(2)

                    # Remove Select All    
                    elem_body.click()

            # Sleep added only for demo, else it is a very bad practice!    
            time.sleep(2)

            # Switching to iFrame using index property
            # Since frames on the test page do not have id property,
            # we won't be demoing this method in the tutorial
            # driver.switch_to.frame(frame_index)

            # Switch back to the main window
            driver.switch_to.default_content()
        except NoSuchElementException:
            print(f"method_name: test failed")
            if exec_platform == 'cloud':
                driver.execute_script("lambda-status=failed")
            pytest.fail(f"{method_name}: Test Failed")