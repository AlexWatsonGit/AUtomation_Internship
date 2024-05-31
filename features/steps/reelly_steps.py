from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

# page = By.CSS_SELECTOR, "https://soft.reelly.io/sign-in"
reely_button = ""
button = 'input[wized="emailInput"]'

test = 'High Demand'
emailbox = By.CSS_SELECTOR, 'input[wized="emailInput"]'
passwordbox = By.CSS_SELECTOR, 'input[wized="passwordInput"]'
@given('Open the webpage')
def Open_the_webpage(context):
    context.driver.get("https://soft.reelly.io/sign-in")
    sleep(2)

@when('Enter login email')
def Enter_login_email(context):
    context.driver.find_element(*emailbox).send_keys('alexwatsonja@gmail.com')
    sleep(2)
@when('Enter login password')
def Enter_login_password(context):
    context.driver.find_element(*passwordbox).send_keys('Gallardo42')
    sleep(1)

@when('click continue')
def click_continue(context):
    context.driver.find_element(By.CSS_SELECTOR, 'a[class="login-button w-button"]').click()
    sleep(5)

@when('click off plan')
def click_off_plan(context):
    context.driver.find_element(By.CSS_SELECTOR, 'a[class="_1-link-menu w-inline-block w--current"]').click()
    sleep(5)

@when('Verify correct page is open')
def verify_correct_page(context):
    context.driver.find_element(By.CSS_SELECTOR, 'div[class="page-title off_plan"]')
    sleep(4)

@when('click on filter icon')
def click_on_filter_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, 'a[class="filter-button w-inline-block"]').click()
    sleep(2)

@when('click on high demand')
def click_high_demand(context):
    context.driver.find_element(By.CSS_SELECTOR, 'div[wized="priorityStatusHighDemand"][class="tag-properties margin-bottom-8"]').click()
    sleep(5)

@then('verify high demand')
def verify_high_demand(context):
    word = context.driver.find_elements(By.CSS_SELECTOR, 'div[class="commision_box"]')
    sleep(2)