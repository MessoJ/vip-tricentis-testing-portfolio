from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        
    def navigate_to_transfer(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[text()='Transfer Funds']"))
        ).click()
        
    def enter_transfer_details(self, account_number, amount):
        self.driver.find_element(By.ID, "recipient_account").send_keys(account_number)
        self.driver.find_element(By.ID, "amount").send_keys(amount)
        
    def submit_transfer(self):
        self.driver.find_element(By.XPATH, "//button[text()='Transfer']").click()
        
    def is_success_message_displayed(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "alert-success"))
        ).is_displayed()
