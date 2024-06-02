from pages.base_page import Page
from selenium.webdriver.common.by import By

class SideBar(Page):
    OFF_PLAN = By.CSS_SELECTOR, 'a[class="_1-link-menu w-inline-block w--current"][aria-current="page"]'
    CORRECTPAGE = By.CSS_SELECTOR, 'div[class="page-title off_plan"]'
    FILTER = By.CSS_SELECTOR, 'a[class="filter-button w-inline-block"]'
    HIGHDEMAND = By.CSS_SELECTOR, By.CSS_SELECTOR, 'div[wized="priorityStatusHighDemand"][class="tag-properties margin-bottom-8"]'

    def click_option(self):
        self.find_element(*self.OFF_PLAN)
        self.find_element(*self.CORRECTPAGE)
        self.click(*self.FILTER)
        self.click(*self.HIGHDEMAND)