import time

from selenium.webdriver.common.by import By

from Modules.GenericPageActions import GenericPageActions


class Browser:

    def __init__(self, browser):
        self.browser = browser


class RevivalStonePage(Browser):
    # Page Locators

    pageTitleAnchor = "Revival Stone (x5)"
    addArrowProperties = (By.CSS_SELECTOR, '.qty-add')
    popUpWindowProperties = (By.CSS_SELECTOR, '.msg-content')
    popUpWindowOkProperties = (By.CSS_SELECTOR, '.btn > a:nth-child(1)')
    anchorTitleProperties = (By.CLASS_NAME, "item-name")

    # Page Functionality
    def check_revivalstone_title_page(self):
        time.sleep(1)
        anchorTitle = GenericPageActions(self.browser).find_object(*RevivalStonePage.anchorTitleProperties).text
        validation = "Revival Stone (x5)" in anchorTitle
        return validation

    def add_item_amount(self, amount):
        addArrow = GenericPageActions(self.browser).find_object(*RevivalStonePage.addArrowProperties)
        for i in range(amount):
            addArrow.click()

    def check_pop_up_message(self, text_to_validate):
        time.sleep(1)
        popUpWindow = GenericPageActions(self.browser).find_object(*RevivalStonePage.popUpWindowProperties)
        popUpWindowText = popUpWindow.text
        print("Text displayed in pop-up: {0}".format(popUpWindowText))
        GenericPageActions(self.browser).take_browser_snapshot \
            ("AIONMarketplace_RevivalStone_PopUp_Message", "png")
        validation = text_to_validate in popUpWindowText
        popUpWindowOk = GenericPageActions(self.browser).find_object(*RevivalStonePage.popUpWindowOkProperties)
        popUpWindowOk.click()
        return validation
