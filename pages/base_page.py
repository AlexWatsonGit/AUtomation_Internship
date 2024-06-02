
class Page:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locator):
        self.driver.find.element(*locator)

    def find_elements(self, *locator):
        self.driver.find.elements(*locator)

    def click(self, *locator):
        self.driver.find.element(*locator).click()

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).sen_keys(text)
