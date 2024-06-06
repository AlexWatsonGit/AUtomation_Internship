from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep
class SideBar(Page):
    OFF_PLAN = By.CSS_SELECTOR, 'a[class="_1-link-menu w-inline-block w--current"][aria-current="page"]'
    CORRECTPAGE = By.CSS_SELECTOR, 'div[class="page-title off_plan"]'
    FILTER = By.CSS_SELECTOR, 'a[class="filter-button w-inline-block"]'
    HIGHDEMAND = By.CSS_SELECTOR, 'div[wized="priorityStatusHighDemand"][class="tag-properties margin-bottom-8"]'

    def navigate_to_highdemand(self):
        sleep(5)
        self.click(*self.OFF_PLAN)
        sleep(3)
        self.find_element(*self.CORRECTPAGE)
        self.click(*self.FILTER)
        sleep(1)
        self.click(*self.HIGHDEMAND)
        sleep(5)