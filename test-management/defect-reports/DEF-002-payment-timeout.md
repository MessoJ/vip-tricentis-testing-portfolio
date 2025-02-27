# DEF-002: Payment Gateway Timeout  
**Severity**: Critical  
**Module**: Checkout  

## Environment:  
- **URL**: https://ecom.example.com/checkout  
- **Browser**: Chrome 118  
- **Test Data**: [transactions.csv](https://gist.github.com/mock-financial-data/345678/raw/transactions.csv)  

## Steps to Reproduce:  
1. Add product `P-101` to cart.  
2. Proceed to checkout.  
3. Enter payment details:  
   - Card: `4111-1111-1111-1111`  
   - Expiry: `12/25`  
4. Click "Pay Now".  

## Actual Result:  
- `504 Gateway Timeout` after 60 seconds.  

## Expected Result:  
- Payment confirmation within 5 seconds.  

## Attachments:  
- [Screenshot](/defect-reports/screenshots/payment-timeout.png)  
- [Logs](/defect-reports/logs/payment-20231010.log)  

## Status:  
🔧 In Progress  
