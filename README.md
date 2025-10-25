# 💸 P2P Loan Default Predictor

A machine learning web application that predicts the likelihood of a borrower defaulting on a P2P (Peer-to-Peer) loan.  
This project uses real Prosper Loan data to analyze borrower behavior, train a predictive model, and deploy it via a Flask web app.

---

## 🚀 Project Overview

This project aims to assist lenders in evaluating the **credit risk** of borrowers using historical loan data.  
It includes complete steps from **data cleaning**, **EDA**, **feature engineering**, **model training**, and **deployment**.

---

## 🧩 Features

- 📊 Exploratory Data Analysis (EDA)  
- 🧹 Data Cleaning and Preprocessing  
- ⚙️ Model Training and Evaluation  
- 💾 Model Serialization (`trained_model.pkl`)  
- 🌐 Flask-based Web App for Prediction  
- 📁 Git LFS for large model and dataset handling

---

## 🧠 Technologies Used

| Category | Tools/Frameworks |
|-----------|------------------|
| Language | Python |
| Data Handling | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-learn |
| Deployment | Flask |
| Version Control | Git, GitHub, Git LFS |

---

## 🧮 Model Building

1. **Data Preprocessing**
   - Missing value treatment
   - Outlier handling
   - Feature encoding and scaling

2. **Modeling**
   - Logistic Regression / Random Forest
   - Hyperparameter tuning
   - Model evaluation (Accuracy, ROC-AUC, Precision, Recall)

3. **Deployment**
   - Model saved as `trained_model.pkl`
   - Flask app accepts user input and returns risk prediction

---

## 📂 Project Structure

<img width="262" height="352" alt="image" src="https://github.com/user-attachments/assets/23121c78-38dd-484b-9d58-6c62d3134469" />



---

## ⚙️ How to Run

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/SUJENPURTY/P2P-Loan-Default-Predictor.git
cd P2P-Loan-Default-Predictor

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run Flask App
python app.py

4️⃣ Open in Browser

Go to: http://127.0.0.1:5000

📈 Future Enhancements

Add feature importance visualization

Include multiple model comparison dashboard

Deploy on Render or AWS EC2

👨‍💻 Author

Sujen Purty
🎓 Quantitative Economics and Data Science, BIT Mesra
💼 Passionate about Data Science, ML, and Model Deployment
🔗 LinkedIn
 | GitHub

⭐ If you like this project, don’t forget to give it a star

