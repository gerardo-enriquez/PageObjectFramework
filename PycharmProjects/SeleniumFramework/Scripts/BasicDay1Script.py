import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

searchBarMap = "lst-ib"
searchButtonMap = "btnK"
textinpagemap = "resultStats"



browser = webdriver.Firefox()
browser.get("http://www.google.com")

searchBar = browser.find_element_by_id(searchBarMap)
searchBar.send_keys("search")
searchButton = browser.find_element_by_name(searchButtonMap)
searchButton.click()

textinpage = browser.find_element_by_id(textinpagemap)
assert "search" in browser.title
browser.quit()