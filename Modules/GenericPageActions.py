import datetime
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


class Browser:

    def __init__(self, browser):
        self.browser = browser


class GenericPageActions(Browser):

    def take_browser_snapshot(self, snapshot_name, snapshot_format):
        picturedate = str(datetime.datetime.today().strftime('%Y_%m_%d'))
        picturename = snapshot_name + picturedate + "." + snapshot_format
        self.browser.save_screenshot(picturename)

    def find_object(self,find_by,locator):
        wait = WebDriverWait(self.browser,10)
        element = None
        try:
            element = wait.until(EC.visibility_of_element_located((find_by,locator)))

        except NoSuchElementException:
            print("Element {0} not found on page".format(locator))

        return element

    def find_objects(self,find_by,locator):
        wait = WebDriverWait(self.browser, 10)
        elements = []
        try:
            elements = wait.until(EC.visibility_of_all_elements_located((find_by,locator)))

        except NoSuchElementException:
            print("Element {0} not found on page".format(locator))

        return elements