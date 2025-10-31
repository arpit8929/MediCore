from flask import Blueprint, render_template, request, send_from_directory
from .app_functions import ValuePredictor
import os
from werkzeug.utils import secure_filename

prediction = Blueprint('prediction', __name__)

UPLOAD_FOLDER = 'uploads'
STATIC_FOLDER = 'static'

dir_path = os.path.dirname(os.path.abspath(__file__))


@prediction.route('/predict', methods=["POST", 'GET'])
def predict():

    if request.method == "POST":
        try:
            # Get form data
            form_data = request.form.to_dict()
            
            # Map form fields to correct order for model: age, gender, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope
            age = float(form_data.get('age', 0))
            gender = float(form_data.get('Gender', 0))  # Note: form uses 'Gender' not 'gender'
            cp = float(form_data.get('cp', 0))
            trestbps = float(form_data.get('trestbps', 0))
            chol = float(form_data.get('chol', 0))
            fbs = float(form_data.get('fbs', 0))
            restecg = float(form_data.get('restecg', 0))
            thalach = float(form_data.get('thalach', 0))
            exang = float(form_data.get('exang', 0))
            oldpeak = float(form_data.get('oldpeak', 0))
            slope = float(form_data.get('slope', 0))
            
            # Create ordered list matching model input (11 features)
            to_predict_list = [
                age, gender, cp, trestbps, chol, fbs, restecg, 
                thalach, exang, oldpeak, slope
            ]
            
            result = ValuePredictor(to_predict_list)
            return render_template("result.html", **result)
            
        except Exception as e:
            print(f"Error in prediction: {str(e)}")
            import traceback
            traceback.print_exc()
            return render_template("result.html", 
                prediction=0,
                risk_percentage=0,
                risk_score=0,
                risk_category="Error",
                heart_age=0,
                actual_age=0,
                risk_factors=[],
                page='heart',
                error_message=str(e),
                future_risk_data=None
            )
    else:
        return render_template('base.html')

## Removed pneumonia upload route as only heart model is used now

@prediction.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)