import requests
import pytest
import json

# Mock API endpoint and test data
API_BASE_URL = "https://api.healthcare-example.com/v1"
TEST_DATA_URL = "https://github.com/MessoJ/vip-tricentis-testing-portfolio/tree/main/automation/healthcare-api-test/data/test_data.json"

@pytest.fixture
def registration_data():
    response = requests.get(TEST_DATA_URL)
    return response.json()

def test_patient_registration(registration_data):
    headers = {"Authorization": "Bearer mock-token-123", "Content-Type": "application/json"}
    
    for patient in registration_data["patients"]:
        response = requests.post(
            f"{API_BASE_URL}/patients",
            headers=headers,
            json={
                "first_name": patient["first_name"],
                "last_name": patient["last_name"],
                "ssn": patient["ssn"]
            }
        )
        
        assert response.status_code == 201, f"Registration failed for {patient['first_name']}"
        assert response.json()["patient_id"] is not None
