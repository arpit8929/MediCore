from flask import Blueprint, render_template, redirect, url_for

views = Blueprint('views', __name__)

@views.route("/")
def home():
    return render_template(r'base.html')
@views.route("/home")
def home_alias():
    return render_template(r'base.html')

@views.route("/service")
def service():
    return redirect(url_for('views.home') + '#service')

@views.route("/contact")
def contact():
    return redirect(url_for('views.home') + '#contact')

@views.route("/heart")
def heart():
    return render_template(r'heart_index.html')

@views.route("/heart_form")
def heart_form():
    return render_template(r'heart.html')