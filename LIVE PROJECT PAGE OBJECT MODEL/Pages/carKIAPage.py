from Pages.BasePage import BasePage

class carKIAPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    
    def goToNewCars(self):
        self.moveTo("newcars_XPATH")
        self.click("findnewcars_XPATH")