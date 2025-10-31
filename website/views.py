from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route("/")
def home():
    return render_template(r'base.html')
@views.route("/heart")
def heart():
    return render_template(r'heart_index.html')

@views.route("/heart_check")
def heart_check():
    return render_template(r'heart_check_intro.html')

@views.route('/recommend/<int:prediction_status>')
def show_recommendation(prediction_status):
   
    # The render_template function automatically looks inside the 'templates' folder.
    # We pass the 'prediction_status' from the URL to a variable named 'prediction' inside the HTML.
    return render_template('recommendations.html', prediction=prediction_status)

@views.route("/heart_form")
def heart_form():
    return render_template(r'heart.html')