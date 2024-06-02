from pages.main_page import MainPage
from pages.side_bar import SideBar
from pages.search_results import SearchResultsPage
class Application:
    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.side_bar = SideBar(driver)
        self.search_results = SearchResultsPage(driver)




