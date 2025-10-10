import pickle
import numpy as np


# --- HEART VALUE PREDICTOR ONLY ---
def ValuePredictor(to_predict_list):
    page = 'heart'
    with open('./website/app_models/heart_model.pkl', 'rb') as f:
        heart_model = pickle.load(f)
    pred = heart_model.predict(np.array(to_predict_list).reshape(1, -1))
    return pred[0], page
