import csv
import pytest
import requests
from selenium import webdriver
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

# Load test data
USER_DATA_URL = "https://gist.githubusercontent.com/mock-banking-data/789012/raw/users.csv"

@pytest.fixture
def user_data():
    response = requests.get(USER_DATA_URL)
    return list(csv.DictReader(response.text.splitlines()))

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_fund_transfer(driver, user_data):
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)
    
    # Use test data
    user = user_data[0]
    
    # Authenticate
    login_page.navigate_to_login()
    login_page.enter_credentials(user["username"], user["password"])
    login_page.submit()
    
    # Perform transfer
    dashboard_page.navigate_to_transfer()
    dashboard_page.enter_transfer_details("ACC-789", "500.00")
    dashboard_page.submit_transfer()
    
    # Verify success
    assert dashboard_page.is_success_message_displayed(), "Transfer failed!"
