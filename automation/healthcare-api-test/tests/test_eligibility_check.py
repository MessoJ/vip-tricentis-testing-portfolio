import requests
import pytest
import json
import responses
import os

# Load mock data
with open("automation/healthcare-api-test/data/test_data.json") as f:
    test_data = json.load(f)

@pytest.mark.parametrize("patient", test_data["patients"])
def test_eligibility_check(patient):
    headers = {"Authorization": "Bearer mock_token"}
    response = requests.post(
        "https://api.healthcare-example.com/v1/eligibility",
        headers=headers,
        json={"patient_id": patient["id"], "service_code": patient["service_code"]}
    )
    
    assert response.status_code == 200
    assert response.json()["eligible"] == patient["eligible"]
