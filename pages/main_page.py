from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep
class MainPage(Page):
    emailbox = By.CSS_SELECTOR, 'input[wized="emailInput"]'
    passwordbox = By.CSS_SELECTOR, 'input[wized="passwordInput"]'
    CONTINUE = By.CSS_SELECTOR, 'a[class="login-button w-button"]'
    password = 'Gallardo42'
    email = 'alexwatsonja@gmail.com'
    def open_main(self):
        self.driver.get("https://soft.reelly.io/sign-in")
        sleep(2)
        self.input_text(self.email, *self.emailbox)
        self.input_text(self.password, *self.passwordbox)
        self.click(*self.CONTINUE)
        sleep(3)