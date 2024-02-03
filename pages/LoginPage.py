from selenium.webdriver.common.by import By
from pages.ClassPage import ClassPage


class LoginPage:

    def __init__(self,driver):
        self.driver = driver

    email_filed_name = "email"
    password_field_name = "password"
    login_button_xpath = "//button[text()='Login']"

    def click_login_button(self, email_address, password):
        self.driver.find_element(By.NAME, self.email_filed_name).send_keys(email_address)
        self.driver.find_element(By.NAME, self.password_field_name).send_keys(password)
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()
        return ClassPage(self.driver)








