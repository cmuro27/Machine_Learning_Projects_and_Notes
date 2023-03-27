import numpy as np
import pickle
from flask import Flask, request, jsonify

def predict_single(customer,model):
    import pandas as pd
    x=pd.DataFrame([customer])
    y_pred = model.predict_proba(x)[:,1]
    return y_pred[0]

with open('churn-model.bin', 'rb') as f_in:
    model = pickle.load(f_in)

customer = {
'customerid': '8879-zkjof',
'gender': 'female', 
'seniorcitizen': 0,
'partner': 'no',
'dependents': 'no',
'tenure': 41,
'phoneservice': 'yes',
'multiplelines': 'no',
'internetservice': 'dsl',
'onlinesecurity': 'yes',
'onlinebackup': 'no',
'deviceprotection': 'yes',
'techsupport': 'yes',
'streamingtv': 'yes',
'streamingmovies': 'yes',
'contract': 'one_year',
'paperlessbilling': 'yes',
'paymentmethod': 'bank_transfer_automatic',
'monthlycharges': 79.85,
'totalcharges': 3320.75,
}

#prediction = predict_single(customer,model)

#print('prediction: %.3f' % prediction)

#if prediction >= 0.5:
#    print('verdict: Churn')
#else:
#    print('verdict: Not churn')    

app = Flask('churn')    
@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()
    prediction = predict_single(customer,model)
    churn = prediction >= 0.5
    result = {'churn_probability': float(prediction),
              'churn': bool(churn)}
    
    return jsonify(result)

# Lines for running Flask app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)