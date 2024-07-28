import streamlit as st

# Title and Description
st.title('LoanGuard: Credit Risk Prediction')
st.write("""
### Welcome to LoanGuard
This app helps predict the credit risk of a borrower based on various factors.
""")

# Age Factor
st.header('Age Factor')
age = st.slider('Select Age', 18, 100, 30)

# Borrower Information
st.header('Borrower Information')
borrower_name = st.text_input('Name')
borrower_id = st.text_input('Borrower ID')

# Credit Score
st.header('Credit Score')
credit_score = st.number_input('Enter Credit Score', min_value=300, max_value=850, value=650)

# Annual Income
st.header('Annual Income')
annual_income = st.number_input('Enter Annual Income', min_value=0, step=1000)

# Loan Amount
st.header('Loan Amount')
loan_amount = st.number_input('Enter Loan Amount', min_value=0, step=1000)

# Payment History
st.header('Payment History')
on_time_payments = st.number_input('Number of On-time Payments', min_value=0, step=1)
late_payments = st.number_input('Number of Late Payments', min_value=0, step=1)
defaulted_payments = st.number_input('Number of Defaulted Payments', min_value=0, step=1)

# Prediction (Placeholder)
st.header('Prediction')
if st.button('Predict Credit Risk'):
    # Placeholder for prediction logic
    st.write('Credit Risk Prediction: [This will be calculated based on your model]')

# Footer
st.write("""
### Disclaimer
This app is for educational purposes only and does not provide actual credit risk assessments.
""")

if __name__ == '__main__':
    st.run()
