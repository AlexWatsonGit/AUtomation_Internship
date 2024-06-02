from selenium.webdriver.common.by import By
from pages.base_page import Page
class MainPage(Page):
    emailbox = By.CSS_SELECTOR, 'input[wized="emailInput"]'
    passwordbox = By.CSS_SELECTOR, 'input[wized="passwordInput"]'
    CONTINUE = By.CSS_SELECTOR, 'a[class="login-button w-button"]'
    password = 'Gallardo42'
    email = 'alexwatsonja@gmail.com'
    def open_main(self):
        self.driver.get("https://soft.reelly.io/sign-in")
        self.find_element(*self.emailbox)
        self.input_text(self.email, *self.emailbox)
        self.find_element(*self.passwordbox)
        self.input_text(self.password, *self.passwordbox)
        self.click(*self.CONTINUE)