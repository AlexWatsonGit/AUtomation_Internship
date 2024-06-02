from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


button = 'input[wized="emailInput"]'
test = 'High Demand'
password = 'Gallardo42'
email = 'alexwatsonja@gmail.com'
emailbox = By.CSS_SELECTOR, 'input[wized="emailInput"]'
passwordbox = By.CSS_SELECTOR, 'input[wized="passwordInput"]'
CONTINUE = By.CSS_SELECTOR, 'a[class="login-button w-button"]'
OFF_PLAN = By.CSS_SELECTOR, 'a[class="_1-link-menu w-inline-block w--current"][aria-current="page"]'
CORRECTPAGE = By.CSS_SELECTOR, 'div[class="page-title off_plan"]'
FILTER = By.CSS_SELECTOR, 'a[class="filter-button w-inline-block"]'
HIGHDEMAND = By.CSS_SELECTOR, 'div[wized="priorityStatusHighDemand"][class="tag-properties margin-bottom-8"]'
HIGHDEMANDTXT = By.CSS_SELECTOR, 'div[class="commision_box"]'

@given('Log in to Reelly_io')
def login_to_reelly(context):
    context.app.main_page.open_main()
@when('Navigate to High Demand filter')
def navigate_to_high_demand_filter(context):
    context.app.side_bar.navigate_to_highdemand()
@then('Verify High demand items are displayed')
def verify_high_demand_items(context):
    context.app.search_results.verify_page()