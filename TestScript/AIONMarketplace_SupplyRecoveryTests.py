import unittest
from selenium import webdriver
from ObjectMap.AIONMarketPlace_HomePage import MarketHomePage
from ObjectMap.AIONMarketPlace_SupplyRecoveryPage import SupplyRecoveryPage
from ObjectMap.AIONMarketPlace_RevivalStone import RevivalStonePage


class AIONmarketPlaceTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://store.aiononline.com/store/index')
        self.driver.implicitly_wait(5)
        self.timeout = 30

    def tearDown(self):
        self.driver.quit()

    def test_AION_marketplace_supply_recovery_revivalstone(self):

        market_home_page = MarketHomePage(self.driver)
        market_home_page.hover_over_supply_menu()
        # 1. Verify that the Supply menu contains a Recovery entry:
        # Since we are able to see it visible and interact with it on the page.
        assert market_home_page.recovery_link_exists()
        supplyrecoverybrowser = market_home_page.navigate_to_supply_recovery_page()
        supply_recovery_page = SupplyRecoveryPage(supplyrecoverybrowser)
        assert supply_recovery_page.check_supply_title_page()
        # 2. Verify that the Revival Stone is present in the list of Recovery items:
        # Once in the correct page, we'll navigate through the items in the page
        # until finding the one that we need. On this case, the revival stone
        supply_recovery_page.scroll_and_find_item_from_list("Revival Stone (x5)")
        revivalstonebrowser = supply_recovery_page.click_on_page_link("Revival Stone (x5)")
        # On the details page for the Revival Stone, verify that the user can't
        # increase the item quantity beyond the maximum. If the user attempts to
        # do so, the following error message should be shown: "This item's maximum
        # purchase quantity per transaction is 10".
        revival_stone_page = RevivalStonePage(revivalstonebrowser)
        assert revival_stone_page.check_revivalstone_title_page()
        revival_stone_page.add_item_amount(10)
        assert revival_stone_page.check_pop_up_message("This item's maximum purchase quantity per transaction is 10")


if __name__ == '__main__':
    unittest.main()
