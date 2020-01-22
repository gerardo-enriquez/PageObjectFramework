from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
url = 'http://www.google.com'

class LaunchBrowser:
    def __init__(self, url):
    self.driver = webdriver.Chrome()
    self.driver.get(url)
    time.sleep(10)

class Browser:
    def __init__(self):
        self.driver = webdriver.Chrome()


LaunchBrowser(url)