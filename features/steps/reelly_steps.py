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
@given('Open the webpage')
def Open_the_webpage(context):
    context.driver.get("https://soft.reelly.io/sign-in")
    sleep(2)
@when('Enter login email')
def Enter_login_email(context):
    context.driver.find_element(*emailbox).send_keys(email)
@when('Enter login password')
def Enter_login_password(context):
    context.driver.find_element(*passwordbox).send_keys(password)
@when('click continue')
def click_continue(context):
    context.driver.find_element(*CONTINUE).click()
    sleep(5)
@when('click off plan')
def click_off_plan(context):
    context.driver.find_element(*OFF_PLAN).click()
    sleep(5)
@when('Verify correct page is open')
def verify_correct_page(context):
    context.driver.find_element(*CORRECTPAGE)
    sleep(4)
@when('click on filter icon')
def click_on_filter_icon(context):
    context.driver.find_element(*FILTER).click()
    sleep(5)

@when('click on high demand')
def click_high_demand(context):
    context.driver.find_element(*HIGHDEMAND).click()
    sleep(5)

@then('verify high demand')
def verify_high_demand(context):
    context.driver.find_elements(*HIGHDEMANDTXT)
    sleep(2)