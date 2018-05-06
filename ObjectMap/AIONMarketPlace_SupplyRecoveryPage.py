import time
from selenium.webdriver.common.by import By
from Modules.GenericPageActions import GenericPageActions


class Browser:

    def __init__(self, browser):
        self.browser = browser


class SupplyRecoveryPage(Browser):
    # Page Locators
    pageTitleAnchor = "Supply  |  Recovery"
    pageTitleCategory = (By.CLASS_NAME,'shop-cat')
    pageTitleType = (By.CLASS_NAME, 'shop-type')
    itemsPerPageLocator = (By.CLASS_NAME, 'item-title')
    nextBtn = (By.CSS_SELECTOR,'.next > span:nth-child(1)')

    # Page Functionality
    def check_supply_title_page(self):
        time.sleep(1)
        pageTitleCategoryElement = GenericPageActions(self.browser).find_object(*SupplyRecoveryPage.pageTitleCategory).text
        pageTitleTypeElement = GenericPageActions(self.browser).find_object(*SupplyRecoveryPage.pageTitleType).text
        validations = ("SUPPLY" in pageTitleCategoryElement) and ("RECOVERY" in pageTitleTypeElement)
        return validations

    def scroll_and_find_item_from_list(self,item_name):
        itemFoundText = None
        itemsPerPageList = []
        while itemFoundText != item_name:
            itemsPerPage = GenericPageActions(self.browser).find_objects(*SupplyRecoveryPage.itemsPerPageLocator)
            for item in itemsPerPage:
                itemsPerPageList.append(item.text)
            if item_name in itemsPerPageList:
                GenericPageActions(self.browser).take_browser_snapshot\
                    ("AIONMarketplace_SupplyRecovery_Itemlist_RevivalStone", "png")
                itemFoundText = self.browser.find_element_by_link_text(item_name).text
                print("Item with name {0} was found".format(itemFoundText))
            else:
                itemsPerPageList = []
                nextButton = GenericPageActions(self.browser).find_object(*SupplyRecoveryPage.nextBtn)
                nextButton.click()
                GenericPageActions(self.browser).find_object(*SupplyRecoveryPage.pageTitleCategory)

    def click_on_page_link(self,link_text):
        link = self.browser.find_element_by_link_text(link_text)
        link.click()
        return self.browser

