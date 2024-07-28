import streamlit as st
import pandas as pd
import joblib

# Title of the app
st.title("LoanGuard: Credit Risk Prediction")

# Sidebar for input
st.sidebar.title("Borrower Information")

# Input fields for borrower features
credit_score = st.sidebar.number_input("Credit Score", min_value=300, max_value=850, value=650)
income = st.sidebar.number_input("Annual Income ($)", min_value=1000, max_value=1000000, value=50000)
loan_amount = st.sidebar.number_input("Loan Amount ($)", min_value=1000, max_value=1000000, value=10000)
payment_history = st.sidebar.selectbox("Payment History", ["Good", "Average", "Poor"])

# Map payment history to numerical values
payment_history_map = {"Good": 0, "Average": 1, "Poor": 2}
payment_history_num = payment_history_map[payment_history]

# Main page for tracking information and displaying results
st.subheader("Entered Borrower Information")
st.write(f"**Credit Score:** {credit_score}")
st.write(f"**Annual Income:** ${income}")
st.write(f"**Loan Amount:** ${loan_amount}")
st.write(f"**Payment History:** {payment_history}")

# Convert input data into a dataframe
input_data = pd.DataFrame({
    'Credit Score': [credit_score],
    'Annual Income': [income],
    'Loan Amount': [loan_amount],
    'Payment History': [payment_history_num]
})

# Predict the default risk
if st.button("Predict Risk"):
    risk_score = model.predict_proba(input_data)[0][1]
    st.write(f"**Predicted Risk Score:** {risk_score:.2f}")

    # Provide recommendations based on risk score
    if risk_score < 0.3:
        st.success("Recommendation: Approve the loan")
    elif risk_score < 0.7:
        st.warning("Recommendation: Consider requesting additional collateral")
    else:
        st.error("Recommendation: Deny the loan")

# Optionally, you can add more functionality like storing the results, etc.
