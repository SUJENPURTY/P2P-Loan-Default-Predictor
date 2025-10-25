from flask import Flask, render_template, request
import numpy as np
import pickle
import datetime

# Initialize Flask app
app = Flask(__name__)
app.debug = True

# Load the trained model
print("Loading regression model...")
with open('model/trained_model.pkl', 'rb') as f:
    rgrmodel = pickle.load(f)
print("Regression model loaded successfully!")

today = datetime.datetime.now()

# Home route
@app.route('/')
def home():
    return render_template('index.html', current_year=today.year)

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Features expected by your RandomForest model
        columns = [
            'CreditGrade', 'Term', 'BorrowerRate', 'LenderYield', 'ProsperScore',
            'EmploymentStatus', 'IsBorrowerHomeowner', 'CurrentCreditLines',
            'OpenRevolvingAccounts', 'InquiriesLast6Months', 'TotalInquiries',
            'BankcardUtilization', 'AvailableBankcardCredit', 'TotalTrades',
            'DebtToIncomeRatio', 'IncomeVerifiable', 'StatedMonthlyIncome',
            'LoanOriginalAmount', 'MonthlyLoanPayment'
        ]

        X = []
        for col in columns:
            val = request.form.get(col)
            if val is None or val == '':
                return render_template('index.html', result=f"Missing input: {col}", current_year=today.year)
            X.append(float(val))

        X = np.array(X).reshape(1, -1)

        # Make prediction
        y_pred = rgrmodel.predict(X)

        result = f"<b>Prediction Result:</b> {y_pred[0]:.2f}"

        return render_template('index.html', result=result, current_year=today.year)

    except Exception as e:
        return render_template('index.html', result=f"Error: {str(e)}", current_year=today.year)

# Run the app
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
