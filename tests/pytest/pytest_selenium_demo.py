import os
import pytest
from os import environ
import time

from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

exec_platform = os.getenv('EXEC_PLATFORM')
time_sleep = 2

########################## Locators #########################
xSubmitForm = "//a[.='Input Form Submit']"
xInpName = "//input[@id='name']"
cInpName = "#name"
xInpEmail = "//form[@id='seleniumform']//input[@name='email']"
xInpPassword = "//input[@name='password']"
cssCompany = "#company"
cWebName = "#websitename"
xInpCountry = "//select[@name='country']"
xInpCity = "//input[@id='inputCity']"
cssAddress1 = "[placeholder='Address 1']"
cssAddress2 = "[placeholder='Address 2']"
cssInpState = "#inputState"
cssInpZip = "#inputZip"
cssInpButton = ".bg-lambda-900"
nameSearchBox = "search"

class TestFormInput:
    def setup_method(self):
        if exec_platform == 'cloud':
            username = environ.get('LT_USERNAME', None)
            access_key = environ.get('LT_ACCESS_KEY', None)

            ch_options = webdriver.ChromeOptions()

            lt_options = {}
            lt_options["build"] = "Build: Getting Started with Selenium PyTest"
            lt_options["project"] = "Project: Getting Started with Selenium PyTest"
            lt_options["name"] = "Test: Getting Started with Selenium PyTest"

            lt_options["browserName"] = "Chrome"
            lt_options["browserVersion"] = "latest"
            lt_options["platformName"] = "macOS Sonoma"
            lt_options["geoLocation"] = "US"

            lt_options["console"] = "error"
            lt_options["w3c"] = True
            lt_options["headless"] = False

            ch_options.set_capability('LT:Options', lt_options)

            gridURL = "https://{}:{}@hub.lambdatest.com/wd/hub".format(username, access_key)
            self.driver = webdriver.Remote(
                command_executor = gridURL,
                options = ch_options
            )
        elif exec_platform == 'local':
            ch_options = ChromeOptions()

            # Refer https://www.selenium.dev/blog/2023/headless-is-going-away/ for the new way
            # to trigger browser in headless mode

            # Enable headless mode for tests like web scraping, API testing, etc.    
            # ch_options.add_argument("--headless=new")
            self.driver = webdriver.Chrome(options=ch_options)

    def test_enter_form_details(self):
        resultant_str = "Thanks for contacting us, we will get back to you shortly."

        driver = self.driver
        driver.get("https://www.lambdatest.com/selenium-playground/")

        # Commented once the tests are executed in non-headless mode
        driver.maximize_window()
        wait = WebDriverWait(driver, 5)

        try:
            element = driver.find_element(By.XPATH, xSubmitForm)
            element.click()

            elem_name = driver.find_element(By.XPATH, xInpName)
            elem_name.send_keys("Testing")
            time.sleep(time_sleep)

            elem_email = driver.find_element(By.XPATH, xInpEmail)
            elem_email.send_keys("testing@testing.com")
            time.sleep(time_sleep)

            elem_pass = driver.find_element(By.XPATH, xInpPassword)
            elem_pass.send_keys("password")
            time.sleep(time_sleep)

            elem_comp = driver.find_element(By.CSS_SELECTOR, cssCompany)
            elem_comp.send_keys("LambdaTest")

            elem = driver.find_element(By.CSS_SELECTOR, cWebName)
            elem.send_keys("https://wwww.lambdatest.com")

            country_dropdown = Select(driver.find_element(By.XPATH, xInpCountry))
            country_dropdown.select_by_visible_text("United States")
            time.sleep(time_sleep)

            elem = driver.find_element(By.XPATH, xInpCity)
            elem.send_keys("San Jose")
            time.sleep(time_sleep)

            elem = driver.find_element(By.CSS_SELECTOR, cssAddress1)
            elem.send_keys("Googleplex, 1600 Amphitheatre Pkwy")
            time.sleep(time_sleep)

            elem = driver.find_element(By.CSS_SELECTOR, cssAddress2)
            elem.send_keys("Mountain View, CA 94043")
            time.sleep(time_sleep)

            elem = driver.find_element(By.CSS_SELECTOR, cssInpState)
            elem.send_keys("California")
            time.sleep(time_sleep)

            elem = driver.find_element(By.CSS_SELECTOR, cssInpZip)
            elem.send_keys("94088")
            time.sleep(time_sleep)

            # Click on the Submit button
            submit_button = driver.find_element(By.CSS_SELECTOR, cssInpButton)
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
            
            time.sleep(2)
        except Exception as e:
            # Catch other exceptions
            print(f"Failed: Input Form Demo, generic exception - {e}")
            if exec_platform == 'cloud':
                driver.execute_script("lambda-status=failed")

        print(f"PyTest Demo: Test Passed")

    def teardown_method(self):
        if (self.driver != None):
            # self.driver.close()
            self.driver.quit()

if __name__ == "__main__":
    pytest.main()