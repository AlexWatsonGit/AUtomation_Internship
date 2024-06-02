from selenium.webdriver.common.by import By
from pages.base_page import Page

class SearchResultsPage(Page):
    HIGHDEMANDTXT = By.CSS_SELECTOR, 'div[class="commision_box"]'
    def verify_page(self):
        self.find_element(*self.HIGHDEMANDTXT)