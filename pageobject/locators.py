from selenium import webdriver
from os import environ
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver import FirefoxOptions

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select

# Not a recommended practice - need to be replaced with Explicit Waits
import time
import pytest

# Imports for Beautiful Soup
import requests
from bs4 import BeautifulSoup

class locators(object):
    test_sel_playground_url = "https://www.lambdatest.com/selenium-playground/"
    test_ecomm_login_playground_url = "https://ecommerce-playground.lambdatest.io/index.php?route=account/login"


    ########## Locators for Selenium playground ##########

    xSubmitForm = "//a[.='Input Form Submit']"
    xInpName = "//input[@id='name']"
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

    ########## Locators for e-commerce playground ##########

    # Credentials - gadetab463@bsidesmn.com and 123456

    cssLoginEmail = "#input-email"
    xLoginPass = "//input[@id='input-password']"
    cssLoginButton = "[value='Login']"

    loginEmail = "gadetab463@bsidesmn.com"
    loginPassword = "123456"

    strPageTitle = "My Account"
    