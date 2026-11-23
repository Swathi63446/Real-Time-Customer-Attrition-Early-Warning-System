from flask import Flask, render_template, request
import pandas as pd
import pickle
import numpy as np
import cohere

app = Flask(__name__)


with open('best_model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)
with open('feature_names.pkl', 'rb') as f:
    feature_names = pickle.load(f)

scale_vars = ["CreditScore", "Age", "Tenure", "Balance", "NumOfProducts", "EstimatedSalary"]


cohere_api_key = os.getenv("COHERE_API_KEY")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
     
        user_input = {
            "CreditScore": float(request.form.get("CreditScore", 0)),
            "Age": float(request.form.get("Age", 0)),
            "Tenure": float(request.form.get("Tenure", 0)),
            "Balance": float(request.form.get("Balance", 0)),
            "NumOfProducts": float(request.form.get("NumOfProducts", 0)),
            "EstimatedSalary": float(request.form.get("EstimatedSalary", 0)),
        }
        
        geo = request.form.get('Geography', 'France')
        user_input['Geography_Germany'] = 1 if geo == 'Germany' else 0
        user_input['Geography_Spain'] = 1 if geo == 'Spain' else 0
  
        gender = request.form.get('Gender', 'Female')
        user_input['Gender_Male'] = 1 if gender == 'Male' else 0
  
        user_input['HasCrCard'] = 1 if request.form.get('HasCrCard') == 'on' else 0
    
        user_input['IsActiveMember'] = 1 if request.form.get('IsActiveMember') == 'on' else 0

        
        input_complete = {feat: user_input.get(feat, 0) for feat in feature_names}
        X_input = pd.DataFrame([input_complete], columns=feature_names)

     
        X_input[scale_vars] = scaler.transform(X_input[scale_vars])

        prob = model.predict_proba(X_input)[0, 1]
        pred = int(prob > 0.3)
        prediction_label = "Churned" if pred == 1 else "Retained"


        auto_prompt = (
            f"A customer with the following attributes: "
            f"Credit Score: {user_input['CreditScore']}, Age: {user_input['Age']}, Tenure: {user_input['Tenure']}, "
            f"Balance: {user_input['Balance']}, Number of Products: {user_input['NumOfProducts']}, "
            f"Estimated Salary: {user_input['EstimatedSalary']}, "
            f"Geography: {geo}, Gender: {gender}, "
            f"Has Credit Card: {'Yes' if user_input['HasCrCard'] else 'No'}, "
            f"Active Member: {'Yes' if user_input['IsActiveMember'] else 'No'}. "
            f"The churn prediction model predicted: '{prediction_label}'. "
            f"Please justify this result based on the input attributes, focusing on the main factors that influence this customer's churn risk."
        )
        try:
            response = co.chat(
                message=auto_prompt,
                model="command-r-plus",  
            )
            justification = response.text
        except Exception as e:
            justification = f"(AI justification unavailable: {e})"

        return render_template(
            'result.html',
            prediction=prediction_label,
            churn_prob=f"{prob:.2%}",
            retain_prob=f"{1-prob:.2%}",
            justification=justification
        )

    return render_template('predict.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

if __name__ == '__main__':
    app.run(debug=False)