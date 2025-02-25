## 🏥 Healthcare API Testing  
### Features  
- **Patient Eligibility Checks**: Validate insurance coverage status.  
- **Patient Registration**: End-to-end registration workflow testing.  
- **Data-Driven Tests**: Uses HIPAA-compliant mock data.  

### Run All Healthcare Tests  
```bash
pytest tests/test_eligibility_check.py tests/test_patient_registration.py -v
