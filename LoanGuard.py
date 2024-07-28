import streamlit as st

st.title('LoanGuard: Credit Risk Prediction')
st.write('This app helps predict the credit risk of a borrower based on various factors.')

# Age Factor
age = st.slider('Select Age', 18, 100)

# Borrower Information
name = st.text_input('Name')
borrower_id = st.text_input('Borrower ID')

# Credit Score
credit_score = st.number_input('Enter Credit Score', min_value=0, max_value=850, value=650)

# Annual Income
annual_income = st.number_input('Enter Annual Income', min_value=0, value=0)

# Loan Amount
loan_amount = st.number_input('Enter Loan Amount', min_value=0, value=0)

# Payment History
on_time_payments = st.number_input('Number of On-time Payments', min_value=0, value=0)
late_payments = st.number_input('Number of Late Payments', min_value=0, value=0)
defaulted_payments = st.number_input('Number of Defaulted Payments', min_value=0, value=0)

# Prediction (Dummy Implementation)
# Replace the following code with actual prediction logic
st.write('## Prediction')
if st.button('Predict'):
    risk_score = (credit_score + annual_income - loan_amount - (late_payments + defaulted_payments * 2)) // 10
    st.write(f'Predicted Credit Risk Score: {risk_score}')

# Disclaimer
st.write('### Disclaimer')
st.write('This app is for educational purposes only and does not provide actual credit risk assessments.')
