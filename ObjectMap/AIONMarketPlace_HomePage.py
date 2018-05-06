import datetime
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from Modules.GenericPageActions import GenericPageActions


class Browser:

    def __init__(self, browser):
        self.browser = browser


class MarketHomePage(Browser):
    # Page Locators
    supplyLink = (By.LINK_TEXT, 'Supply')
    windowRecoveryLink = (By.LINK_TEXT, 'Recovery')

    # Page Functionality
    def hover_over_supply_menu(self):
        supplylinkelement = GenericPageActions(self.browser).find_object(*MarketHomePage.supplyLink)
        self.browser.execute_script("arguments[0].scrollIntoView();", supplylinkelement)
        actions = ActionChains(self.browser)
        hoverelement = actions.move_to_element(supplylinkelement)
        hoverelement.perform()
        time.sleep(2)
        GenericPageActions(self.browser).take_browser_snapshot\
            ("AIONMarketplace_SupplyList_Recovery_","png")

    def recovery_link_exists(self):
        recoveryLink = GenericPageActions(self.browser).find_object(*MarketHomePage.windowRecoveryLink)
        return recoveryLink.is_displayed()

    def navigate_to_supply_recovery_page(self):
        windowrecoverylink = GenericPageActions(self.browser).find_object(*MarketHomePage.windowRecoveryLink)
        windowrecoverylink.click()
        return self.browser


