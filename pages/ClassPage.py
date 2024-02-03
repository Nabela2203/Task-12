from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class ClassPage:

    def __init__(self,driver):
        self.driver = driver

    class_text_xpath = "//h1[text()='Class']"
    profile_icon_class_name = "profileIcon"
    logout_xpath = "//button[text()='Logout']"

    def class_text_is_displayed(self):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.class_text_xpath)))

    def click_on_logout(self):
        self.driver.find_element(By.CLASS_NAME, self.profile_icon_class_name).click()
        self.driver.find_element(By.XPATH, self.logout_xpath).click()

    def refresh_page(self):
        self.driver.refresh()







