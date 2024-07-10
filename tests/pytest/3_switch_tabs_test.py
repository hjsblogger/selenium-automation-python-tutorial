# Import the locators file
import sys
sys.path.append(sys.path[0] + "/../..")
from pageobject.locators import locators
from pageobject.locators import *

from pageobject.helpers import helpers
from pageobject.helpers import *

@pytest.mark.usefixtures('driver')

class TestSwitchTabsDemo:
    def test_switch_tabs_demo(self, driver):
        driver.get(locators.test_sel_playground_url)
        driver.maximize_window()

        window1_title = driver.title
        print(f"Window - 1 title is '{window1_title}'")

        # Get the current window handle
        print("Window - 1 Handle : " + str(driver.window_handles[0]))

        # Open up a new tab and switch to it
        #https://www.selenium.dev/documentation/webdriver/interactions/windows/
        # #create-new-window-or-new-tab-and-switch
        driver.switch_to.new_window('tab')

        # Modify the above line to open a new window
        driver.switch_to.new_window('window')

        time.sleep(4)
        driver.get(locators.test_ecomm_login_playground_url)

        window2_title = driver.title
        print(f"Window - 2 title is '{window2_title}'")

        # Get the current window handle
        print("Window - 2 Handle : " + str(driver.window_handles[1]))


        # Close the current window
        driver.close()

        # Now switch to the earlier window and than close it
        driver.switch_to.window(driver.window_handles[0])

        # Only for testing
        driver.close()

        print("Switching windows test complete")