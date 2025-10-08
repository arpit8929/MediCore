import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"  # Force CPU usage

import pickle
import numpy as np
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.models import load_model
from werkzeug.utils import secure_filename
from sklearn.preprocessing import StandardScaler
import xgboost

# --- MODEL LOADER (patched for DepthwiseConv2D issue) ---
def get_model(path):
    from keras.models import load_model
    from keras.layers import DepthwiseConv2D

    class PatchedDepthwiseConv2D(DepthwiseConv2D):
        def __init__(self, *args, **kwargs):
            kwargs.pop('groups', None)  # Ignore 'groups' argument
            super().__init__(*args, **kwargs)

    model = load_model(path, compile=False, custom_objects={'DepthwiseConv2D': PatchedDepthwiseConv2D})
    return model

# --- IMAGE PREDICTOR (for Pneumonia model) ---
def pred(path):
    data = load_img(path, target_size=(224, 224))  # <-- Change here to (224, 224)
    data = np.asarray(data).reshape((-1, 224, 224, 3))  # <-- Update reshape too
    data = data * 1.0 / 255
    predicted = np.round(get_model('./website/app_models/pneumonia_model.h5').predict(data)[0])[0]
    return predicted


# --- TABULAR VALUE PREDICTOR (kidney, liver, heart, stroke, diabetes) ---
def ValuePredictor(to_predict_list):
    pred = None
    page = ''

    if len(to_predict_list) == 15:
        page = 'kidney'
        with open('./website/app_models/kidney_model.pkl', 'rb') as f:
            kidney_model = pickle.load(f)
        pred = kidney_model.predict(np.array(to_predict_list).reshape(1, -1))

    elif len(to_predict_list) == 10:
        page = 'liver'
        with open('./website/app_models/liver_model.pkl', 'rb') as f:
            liver_model = pickle.load(f)
        pred = liver_model.predict(np.array(to_predict_list).reshape(1, -1))

    elif len(to_predict_list) == 11:
        page = 'heart'
        with open('./website/app_models/heart_model.pkl', 'rb') as f:
            heart_model = pickle.load(f)
        pred = heart_model.predict(np.array(to_predict_list).reshape(1, -1))

    elif len(to_predict_list) == 9:
        page = 'stroke'
        with open('./website/app_models/avc_scaler.pkl', 'rb') as f:
            stroke_scaler = pickle.load(f)
        l1 = np.array(to_predict_list[2:]).reshape(1, -1).tolist()[0]
        l2 = stroke_scaler.transform(np.array(to_predict_list[0:2]).reshape(1, -1)).tolist()[0]
        combined_input = l2 + l1
        with open('./website/app_models/avc_model.pkl', 'rb') as f:
            stroke_model = pickle.load(f)
        pred = stroke_model.predict(np.array(combined_input).reshape(1, -1))

    elif len(to_predict_list) == 8:
        page = 'diabete'
        with open('./website/app_models/diabete_model.pkl', 'rb') as f:
            diabete_model = pickle.load(f)
        pred = diabete_model.predict(np.array(to_predict_list).reshape(1, -1))
        print(pred[0], page)

    return pred[0], page
