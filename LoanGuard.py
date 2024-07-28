import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('credit_risk_model.pkl')

# Streamlit app
def main():
    st.title("LoanGuard: Credit Risk Prediction")

    # Input fields for borrower features
    credit_score = st.number_input("Credit Score", min_value=300, max_value=850, value=650)
    income = st.number_input("Annual Income", min_value=1000, max_value=1000000, value=50000)
    loan_amount = st.number_input("Loan Amount", min_value=1000, max_value=1000000, value=10000)
    payment_history = st.selectbox("Payment History", ["Good", "Average", "Poor"])
    
    # Map payment history to numerical values
    payment_history_map = {"Good": 0, "Average": 1, "Poor": 2}
    payment_history = payment_history_map[payment_history]

    # Convert input data into a dataframe
    input_data = pd.DataFrame({
        'Credit Score': [credit_score],
        'Annual Income': [income],
        'Loan Amount': [loan_amount],
        'Payment History': [payment_history]
    })

    # Predict the default risk
    if st.button("Predict Risk"):
        risk_score = model.predict_proba(input_data)[0][1]
        st.write(f"Predicted Risk Score: {risk_score:.2f}")

        # Provide recommendations based on risk score
        if risk_score < 0.3:
            st.success("Recommendation: Approve the loan")
        elif risk_score < 0.7:
            st.warning("Recommendation: Consider requesting additional collateral")
        else:
            st.error("Recommendation: Deny the loan")

if __name__ == '__main__':
    main()

