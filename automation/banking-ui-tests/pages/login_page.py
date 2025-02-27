from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://banking.example.com/login"
        
    def navigate_to_login(self):
        self.driver.get(self.url)
        
    def enter_credentials(self, username, password):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        ).send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        
    def submit(self):
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
