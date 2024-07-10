import sys
import os
from os import environ
sys.path.append(sys.path[0] + "/../..")
from pageobject.locators import locators
from pageobject.locators import *

exec_platform = os.getenv('EXEC_PLATFORM')

class pyunit_setup:    
    def __init__(self):
        if exec_platform == 'cloud':
            username = environ.get('LT_USERNAME', None)
            access_key = environ.get('LT_ACCESS_KEY', None)

            ch_options = webdriver.ChromeOptions()

            lt_options = {}
            lt_options["build"] = "Build: Getting Started with Selenium Python"
            lt_options["project"] = "Project: Getting Started with Selenium Python"
            lt_options["name"] = "Test: Getting Started with Selenium Python"

            lt_options["browserName"] = "Chrome"
            lt_options["browserVersion"] = "latest"
            lt_options["platformName"] = "macOS Sonoma"

            lt_options["console"] = "error"
            lt_options["w3c"] = True
            lt_options["headless"] = False

            ch_options.set_capability('LT:Options', lt_options)

            gridURL = "https://{}:{}@hub.lambdatest.com/wd/hub".format(username, access_key)
            self.browser = webdriver.Remote(
                command_executor = gridURL,
                options = ch_options
            )
        elif exec_platform == 'local':
            ch_options = ChromeOptions()

            # Refer https://www.selenium.dev/blog/2023/headless-is-going-away/ for the new way
            # to trigger browser in headless mode

            # Enable headless mode for tests like web scraping, API testing, etc.    
            # ch_options.add_argument("--headless=new")
            self.browser = webdriver.Chrome(options=ch_options)
  
    def setUp(self):
        self.browser.implicitly_wait(10)
        self.browser.maximize_window()

    def tearDown(self):
        if (self.browser != None):
            self.browser.quit()