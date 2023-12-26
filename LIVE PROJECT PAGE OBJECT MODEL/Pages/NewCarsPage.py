from Pages.BasePage import BasePage

class NewCarsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def selectKIA(self):
        self.click("new_car_KIA_XPATH")

    def selectHonda(self):
        self.click("new_car_Honda_XPATH")

    def selectBMW(self):
        self.click("new_car_BMW_XPATH")

