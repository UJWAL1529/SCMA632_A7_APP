# LoanGuard: Credit Risk Prediction

Welcome to LoanGuard! This application is designed to help predict the credit risk of a borrower based on various factors such as age, credit score, annual income, loan amount, and payment history.

## Features

- **Age Factor**: Select the borrower's age using an interactive slider.
- **Borrower Information**: Enter the borrower's name and ID.
- **Credit Score**: Input the borrower's credit score within a specified range.
- **Annual Income**: Input the borrower's annual income.
- **Loan Amount**: Input the desired loan amount.
- **Payment History**: Enter the number of on-time, late, and defaulted payments.
- **Credit Risk Prediction**: Placeholder for the credit risk prediction logic which will be calculated based on the provided data.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/loanguard.git
   cd loanguard

python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

pip install -r requirements.txt

streamlit run loanguard.py

