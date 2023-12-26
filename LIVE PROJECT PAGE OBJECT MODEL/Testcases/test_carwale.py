import pytest
import logging
from Pages.BasePage import BasePage
from Pages.HomePage import HomePage
from Utilities.LogUtil import Logger
import time

log = Logger(__name__, logging.INFO)

class Test_Carwale(BasePage):

    def test_gotoNewCr(self):
        log.logger.info("********* Inside New Care Test ***********")
        home = HomePage(self.driver)
        home.goToNewCars()
        time.sleep(5)
