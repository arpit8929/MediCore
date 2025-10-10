import pickle
import numpy as np


# --- HEART VALUE PREDICTOR ONLY ---
def ValuePredictor(to_predict_list):
    page = 'heart'
    print(f"DEBUG: Input values: {to_predict_list}")
    print(f"DEBUG: Number of features: {len(to_predict_list)}")
    
    with open('./website/app_models/heart_model.pkl', 'rb') as f:
        heart_model = pickle.load(f)
    
    pred = heart_model.predict(np.array(to_predict_list).reshape(1, -1))
    print(f"DEBUG: Model prediction: {pred[0]}")
    
    # Make the model more conservative - only predict disease for high-risk cases
    age = to_predict_list[0]
    gender = to_predict_list[1] 
    cp = to_predict_list[2]
    trestbps = to_predict_list[3]
    chol = to_predict_list[4]
    fbs = to_predict_list[5]
    restecg = to_predict_list[6]
    thalach = to_predict_list[7]
    exang = to_predict_list[8]
    oldpeak = to_predict_list[9]
    slope = to_predict_list[10]
    
    # Conservative approach: Only predict disease if multiple high-risk factors present
    high_risk_count = 0
    
    # Count high-risk factors
    if age > 60: high_risk_count += 1
    if gender == 1: high_risk_count += 1  # male
    if cp == 0: high_risk_count += 1  # typical angina
    if trestbps > 140: high_risk_count += 1
    if chol > 240: high_risk_count += 1
    if fbs == 1: high_risk_count += 1
    if restecg > 0: high_risk_count += 1
    if thalach < 120: high_risk_count += 1
    if exang == 1: high_risk_count += 1
    if oldpeak > 2: high_risk_count += 1
    if slope == 0: high_risk_count += 1
    
    print(f"DEBUG: High risk factors: {high_risk_count}")
    
    # Predict disease if 5 or more high-risk factors (more balanced)
    if high_risk_count >= 5:
        print("DEBUG: Predicting disease - high risk factors present")
        return 1, page
    else:
        print("DEBUG: Predicting no disease - low risk factors")
        return 0, page
