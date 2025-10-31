from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os, random


db = SQLAlchemy()
DB_NAME = 'database.db'



def create_app():
    app = Flask(__name__)
    random.seed(0)
    app.config['SECRET_KEY'] = os.urandom(24)
    # For Vercel, use /tmp for writable files (instance folder may not be writable)
    if os.environ.get('VERCEL'):
        instance_path = '/tmp'
    else:
        instance_path = app.instance_path
        os.makedirs(instance_path, exist_ok=True)
    db_path = os.path.join(instance_path, DB_NAME)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.init_app(app)

    from .views import views
    from .prediction import prediction
    from .messages import messages
    

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(prediction, url_prefix='/')
    app.register_blueprint(messages, url_prefix='/')

    from .models import Messages

    create_database(app)



    return app


def create_database(app):
    # Ensure all tables exist in the configured database. Idempotent for SQLite.
    with app.app_context():
        db.create_all()

