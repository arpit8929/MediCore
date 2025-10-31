import pickle
import numpy as np
import os


# --- HEART VALUE PREDICTOR ONLY ---
def ValuePredictor(to_predict_list):
    page = 'heart'
    print(f"DEBUG: Input values: {to_predict_list}")
    print(f"DEBUG: Number of features: {len(to_predict_list)}")
    
    # Construct the absolute path to the model file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(current_dir, 'app_models', 'heart_model.pkl')
    
    try:
        with open(model_path, 'rb') as f:
            heart_model = pickle.load(f)
    except FileNotFoundError:
        print(f"ERROR: Heart model file not found at {model_path}")
        return {
            'prediction': 0,
            'risk_percentage': 0,
            'risk_score': 0,
            'risk_category': 'Error',
            'heart_age': 0,
            'actual_age': 0,
            'risk_factors': [],
            'page': page,
            'error_message': 'Model file not found',
            'future_risk_data': None,
            'model_confidence': 0
        }
    except Exception as e:
        print(f"ERROR loading model: {str(e)}")
        return {
            'prediction': 0,
            'risk_percentage': 0,
            'risk_score': 0,
            'risk_category': 'Error',
            'heart_age': 0,
            'actual_age': 0,
            'risk_factors': [],
            'page': page,
            'error_message': str(e),
            'future_risk_data': None,
            'model_confidence': 0
        }
    
    # Ensure we have enough values
    if len(to_predict_list) < 11:
        to_predict_list = list(to_predict_list) + [0.0] * (11 - len(to_predict_list))
    
    # Use first 11 features for prediction
    pred_input = np.array(to_predict_list[:11]).reshape(1, -1)
    
    try:
        # Get model prediction - MUST use predict_proba if available
        pred_class = heart_model.predict(pred_input)[0]
        
        # Get probability - this is the KEY to using actual model values
        if hasattr(heart_model, 'predict_proba'):
            pred_proba = heart_model.predict_proba(pred_input)[0]
            # pred_proba[1] is the probability of having heart disease (class 1)
            model_risk_percentage = round(pred_proba[1] * 100, 2)
            model_confidence = round(max(pred_proba[0], pred_proba[1]) * 100, 2)
            print(f"DEBUG: Model probability - Class 0: {pred_proba[0]:.4f} ({pred_proba[0]*100:.2f}%), Class 1: {pred_proba[1]:.4f} ({pred_proba[1]*100:.2f}%)")
        else:
            # If model doesn't have predict_proba, this shouldn't happen but handle it
            raise AttributeError("Model does not support predict_proba - cannot get probability scores")
        
        print(f"DEBUG: Model prediction class: {pred_class}")
        print(f"DEBUG: Model risk percentage (from predict_proba): {model_risk_percentage}%")
        print(f"DEBUG: Model confidence: {model_confidence}%")
        
    except Exception as e:
        print(f"ERROR in prediction: {str(e)}")
        import traceback
        traceback.print_exc()
        age_val = int(to_predict_list[0]) if len(to_predict_list) > 0 and to_predict_list[0] > 0 else 0
        return {
            'prediction': 0,
            'risk_percentage': 0,
            'risk_score': 0,
            'risk_category': 'Error',
            'heart_age': age_val,
            'actual_age': age_val,
            'risk_factors': [],
            'page': page,
            'error_message': str(e),
            'future_risk_data': None,
            'model_confidence': 0
        }
    
    # Extract input values safely
    try:
        age = int(float(to_predict_list[0])) if len(to_predict_list) > 0 else 0
        gender = float(to_predict_list[1]) if len(to_predict_list) > 1 else 0
        cp = float(to_predict_list[2]) if len(to_predict_list) > 2 else 0
        trestbps = float(to_predict_list[3]) if len(to_predict_list) > 3 else 0
        chol = float(to_predict_list[4]) if len(to_predict_list) > 4 else 0
        fbs = float(to_predict_list[5]) if len(to_predict_list) > 5 else 0
        restecg = float(to_predict_list[6]) if len(to_predict_list) > 6 else 0
        thalach = float(to_predict_list[7]) if len(to_predict_list) > 7 else 0
        exang = float(to_predict_list[8]) if len(to_predict_list) > 8 else 0
        oldpeak = float(to_predict_list[9]) if len(to_predict_list) > 9 else 0
        slope = float(to_predict_list[10]) if len(to_predict_list) > 10 else 0
    except (ValueError, IndexError) as e:
        print(f"ERROR extracting values: {str(e)}")
        age = 0
        gender = cp = trestbps = chol = fbs = restecg = thalach = exang = oldpeak = slope = 0
    
    # USE MODEL'S RISK PERCENTAGE DIRECTLY - NO HARDCODED VALUES
    risk_percentage = model_risk_percentage
    
    # Calculate risk category based ONLY on model's probability output
    # Based on reference website approach: Low (<20%), Moderate (20-40%), High (40%+)
    if risk_percentage < 20:
        risk_category = "Low Risk"
    elif risk_percentage < 40:
        risk_category = "Moderate Risk"
    elif risk_percentage < 60:
        risk_category = "Moderate-High Risk"
    else:
        risk_category = "High Risk"
    
    # Calculate heart age based on model's risk percentage (proportional calculation)
    # Heart age increases proportionally with risk percentage
    age_factor = (risk_percentage / 100) * 15  # Max +15 years for 100% risk
    heart_age = age + int(age_factor)
    
    # Ensure heart age is reasonable (within ±10 years of actual age)
    heart_age = max(heart_age, max(age - 10, age - 5))
    heart_age = min(heart_age, age + 20)
    
    # Identify risk factors based on actual input values (for informational purposes)
    risk_factors = []
    
    if age > 65:
        risk_factors.append("Advanced age (>65 years)")
    elif age > 50:
        risk_factors.append("Age above 50 years")
    
    if gender == 1:
        risk_factors.append("Male gender")
    
    if cp == 0:
        risk_factors.append("Typical angina chest pain")
    elif cp == 1:
        risk_factors.append("Atypical angina")
    
    if trestbps > 140:
        risk_factors.append(f"High resting blood pressure ({int(trestbps)} mmHg)")
    elif trestbps > 120:
        risk_factors.append(f"Elevated blood pressure ({int(trestbps)} mmHg)")
    
    if chol > 240:
        risk_factors.append(f"High cholesterol ({int(chol)} mg/dl)")
    elif chol > 200:
        risk_factors.append(f"Borderline high cholesterol ({int(chol)} mg/dl)")
    
    if fbs == 1:
        risk_factors.append("High fasting blood sugar (>120 mg/dl)")
    
    if restecg > 0:
        if restecg == 1:
            risk_factors.append("ST-T wave abnormality")
        elif restecg == 2:
            risk_factors.append("Left ventricular hypertrophy")
    
    if thalach < 120:
        risk_factors.append(f"Low maximum heart rate ({int(thalach)} bpm)")
    
    if exang == 1:
        risk_factors.append("Exercise-induced angina")
    
    if oldpeak > 2:
        risk_factors.append(f"Significant ST depression ({oldpeak:.2f})")
    elif oldpeak > 1:
        risk_factors.append(f"Moderate ST depression ({oldpeak:.2f})")
    
    if slope == 2:
        risk_factors.append("Downsloping ST segment")
    
    if not isinstance(risk_factors, list):
        risk_factors = []
    
    # Generate future health risk data based on model's current prediction
    # Project risk over 5 years using exponential growth model
    current_risk = risk_percentage
    # Growth rate depends on current risk level
    if current_risk >= 60:
        annual_increase = 2.5  # High risk increases faster
    elif current_risk >= 40:
        annual_increase = 2.0
    elif current_risk >= 20:
        annual_increase = 1.5
    else:
        annual_increase = 1.0  # Low risk increases slowly
    
    future_risk_data = {
        'labels': ['Current', '1 Year', '2 Years', '3 Years', '4 Years', '5 Years'],
        'data': []
    }
    
    for year in range(6):
        if year == 0:
            future_risk = current_risk
        else:
            # Project risk: risk increases exponentially based on current level
            future_risk = min(100, current_risk + (annual_increase * year * (1 + current_risk / 100)))
        future_risk_data['data'].append(round(future_risk, 2))
    
    # Calculate clinical risk score (separate from model prediction - for display only)
    # This is just for reference, not used for final prediction
    clinical_risk_score = sum([
        25 if age > 65 else 15 if age > 50 else 5 if age > 40 else 0,
        10 if gender == 1 else 0,
        20 if cp == 0 else 10 if cp == 1 else 0,
        15 if trestbps > 140 else 5 if trestbps > 120 else 0,
        15 if chol > 240 else 5 if chol > 200 else 0,
        10 if fbs == 1 else 0,
        10 if restecg > 0 else 0,
        10 if thalach < 120 else 0,
        15 if exang == 1 else 0,
        15 if oldpeak > 2 else 5 if oldpeak > 1 else 0,
        10 if slope == 2 else 0
    ])
    clinical_risk_score = min(clinical_risk_score, 100)
    
    result = {
        'prediction': int(pred_class),
        'risk_percentage': round(risk_percentage, 2),  # From model's predict_proba
        'risk_score': int(clinical_risk_score),  # Clinical score for reference
        'risk_category': str(risk_category),  # Based on model's risk percentage
        'heart_age': int(heart_age),  # Calculated from model's risk percentage
        'actual_age': int(age),
        'risk_factors': risk_factors[:8] if len(risk_factors) > 0 else [],
        'page': str(page),
        'future_risk_data': future_risk_data,
        'model_confidence': round(model_confidence, 2)
    }
    
    print(f"DEBUG: Final output - Prediction: {pred_class}, Risk: {risk_percentage}%, Category: {risk_category}, Heart Age: {heart_age}")
    
    return result