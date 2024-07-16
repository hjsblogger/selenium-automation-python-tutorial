# Import the locators file
import sys

from pageobject.locators import locators
from pageobject.locators import *

def create_actions(driver) -> ActionChains:
    actions = ActionChains(driver)
    return actions

def create_waits(driver: WebDriver, duration: int) -> WebDriverWait:
    # Explicit wait of 10 seconds
    wait = WebDriverWait(driver, duration)
    return wait

def locate_element(driver: WebDriver, by: By, locator: str) -> WebElement:
    try:
        web_element = driver.find_element(by, locator)
        return web_element
    except NoSuchElementException:
        print(f"Element not found")
        return None
    
def dropdown_select_element(select_dropdown: Select, method_name: str, 
        *args, **kwargs) -> None:
    if method_name == "visible_text":
        select_dropdown.select_by_visible_text(args[0])
    elif method_name == "select_value":
        select_dropdown.select_by_value(args[0])
    elif method_name == "select_index":
        select_dropdown.select_by_index(args[0])

    return

def print_select_element(select_dropdown: Select, method_name: str) -> None:
    
    # def all_selected_options(self) -> List[WebElement]:
    selected_options = select_dropdown.all_selected_options

    # Print the text of each selected option
    for option in selected_options:
        print(f"'{method_name}': Selected options text:", option.text)

    # Deselect all the values
    select_dropdown.deselect_all()
    return
    
def locate_elements(driver: WebDriver, by: By, locator: str) -> list:
    try:
        web_element_list = driver.find_elements(by, locator)
        return web_element_list
    except NoSuchElementException:
        print(f"Elements not found")
        return None
    
def locate_elements_gen(element: WebElement, by: By, locator: str) -> list:
    try:
        web_element_list = element.find_elements(by, locator)
        return web_element_list
    except NoSuchElementException:
        print(f"Elements not found")
        return None

def enter_details(driver: WebDriver, by: By, locator: str,
                input: str, sleep_time: int) -> None:
    try:
        key_str = driver.find_element(by, locator)
        key_str.send_keys(input)
        time.sleep(sleep_time)
    except Exception as e:
        print(f"An error occurred: {e}")


class helpers(object):
    def scrap_ecomm_content(driver)->list:
        meta_data_arr=[]
        # Explicit wait of 10 seconds
        wait = create_waits(driver, 10)

        actions = create_actions(driver)

        # Wait for the element to visible, it will be interactable once it is visible
        # element_cat = driver.find_element(By.XPATH, "//a[contains(.,'Shop by Category')]")
        element_cat = wait.until(EC.visibility_of_element_located((By.XPATH,
                locators.shopcategory)))

        # Move to the element and perform click operation
        actions.move_to_element(element_cat).click().perform()

        # element_category = driver.find_element(By.XPATH, "//span[contains(.,'Phone, Tablets & Ipod')]")
        element_phcat = wait.until(EC.visibility_of_element_located((By.XPATH,
                locators.phonecategory)))

        actions.move_to_element(element_phcat).click().perform()

        # Better to wait till the respective element is visible
        # Tough nut : 1 - nested locators!
        nested_elements = wait.until(EC.visibility_of_element_located((By.XPATH,
            "//div[@id='entry_212391']//div[@id='entry_212408']//div[@class='row']")))

        # Tough nut : 2 - nested locators!
        actual_items = nested_elements.find_elements(By.CLASS_NAME,
                "product-layout.product-grid.no-desc.col-xl-4.col-lg-4.col-md-4.col-sm-6.col-6")

        count = len(actual_items)
        # print("Number of elements found:" + str(count) + ".\n")

        for ind_elem_props in actual_items:
            # nested_img_elem = ind_elem_props.find_element(By.CSS_SELECTOR,
            #    "div.product-thumb > div.product-thumb-top > div.image")
            
            ################ Product Image Link ################
            # item_image = nested_img_elem.find_element(By.XPATH,
            #    "//*[contains(@id, 'mz-product-grid-image')]")

            nested_product_name_elem = ind_elem_props.find_element(By.CSS_SELECTOR,
                "div.product-thumb > div.caption")
            
            ################ Product Name ################
            nested_title_elem = nested_product_name_elem.find_element(By.CSS_SELECTOR,
                    ".title .text-ellipsis-2")
            
            ################ Price #######################
            nested_price_elem = nested_product_name_elem.find_element(By.CSS_SELECTOR,
                    ".price .price-new")
            
            # Create a dictionary of the meta-data of the items on e-commerce store
            meta_data_dict = {
                'product image': nested_title_elem.get_attribute('href'),
                'product name': nested_title_elem.text,
                'product price': nested_price_elem.text
            }
            
            meta_data_arr.append(meta_data_dict)
        
        return meta_data_arr
    
    def scrap_yt_content(driver)->list:
        meta_data_arr=[]
        # Explicit wait of 10 seconds
        wait = create_waits(driver, 10)

        actions = create_actions(driver)

        # Explicit wait of 10 seconds
        wait = WebDriverWait(driver, 10)

        # Wait for 10 seconds till the Document State is not complete
        wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')

        # Once the page has loaded, scroll to the end of the page to load all the videos
        # Scroll to the end of the page to load all the videos in the channel
        # Reference - https://stackoverflow.com/a/51702698/126105
        # Get scroll height
        start_height = driver.execute_script("return document.documentElement.scrollHeight")

        # Repeat scrolling until reaching the end of the page
        # Taking cues from my own blog https://www.lambdatest.com/blog/scraping-dynamic-web-pages/
        while True:
            # Scroll to the bottom of the page
            driver.execute_script("window.scrollTo(0, " + str(start_height) + ")")
            # Wait for the content to load
            time.sleep(2)
            scroll_height = driver.execute_script("return document.documentElement.scrollHeight")
            if (scroll_height == start_height):
                # If heights are the same, we reached the end of page
                break
            # print("scroll_height = " + str(scroll_height))
            time.sleep(2)
            start_height = scroll_height

        time.sleep(2)

        elem_1 = driver.find_elements(By.CSS_SELECTOR,
            "#dismissible > #details")

        for video_metadata_1 in elem_1:
            elem_2 = video_metadata_1.find_element(By.CSS_SELECTOR,
                "#meta")

            elem_3 = elem_2.find_element(By.CSS_SELECTOR,
                "#video-title")

            elem_4 = elem_2.find_element(By.CSS_SELECTOR,
                "#metadata > #metadata-line > span:nth-child(3)")

            elem_5 = elem_2.find_element(By.CSS_SELECTOR,
                "#metadata > #metadata-line > span:nth-child(4)")

            video_title = elem_3.get_attribute('innerText')
            video_views = elem_4.get_attribute('innerText')
            video_time = elem_5.get_attribute('innerText')

            # Create a dictionary of the video meta-data
            meta_data_dict = {
                'video title': video_title,
                'video views': video_views,
                'video duration': video_time
            }

            meta_data_arr.append(meta_data_dict)

        return meta_data_arr

    def print_scrapped_content(meta_data):
        for elem_info in meta_data:
            print(elem_info)