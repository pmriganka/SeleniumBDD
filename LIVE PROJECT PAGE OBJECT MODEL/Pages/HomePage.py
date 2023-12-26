from Pages.BasePage import BasePage

class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    
    def goToNewCars(self):
        self.moveTo("newcars_XPATH")
        self.click("findnewcars_XPATH")

    def goToCompareCars(self):
        pass

    def goToUsedCars(self):
        pass

