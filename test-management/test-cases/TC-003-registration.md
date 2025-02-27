# TC-003: Patient Registration Validation  
**Priority**: High  
**Module**: Registration  

## Test Data  
[patients.csv](https://gist.github.com/mock-healthcare-data/123456/raw/patients.csv)  

## Steps:  
1. Navigate to registration page.  
2. Enter patient details:  
   - First Name: `John`  
   - Last Name: `Doe`  
   - SSN: `123-45-6789`  
3. Click "Submit".  

## Expected Result:  
- Patient ID is generated.  
- Confirmation email is sent.  

## Status:  
✅ Pass (2023-10-10)  
