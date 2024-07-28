import streamlit as st
import pandas as pd
import joblib

# Load the trained model
try:
    model = joblib.load('credit_risk_model.pkl')
except FileNotFoundError:
    st.error("Model file not found. Please ensure 'credit_risk_model.pkl' is present in the app directory.")
    st.stop()

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

# Main page for track
