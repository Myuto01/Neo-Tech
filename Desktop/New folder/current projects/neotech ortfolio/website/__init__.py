from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from .models import Meeting

db = SQLAlchemy()
DB_NAME = 'meetings.db'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "james bond"
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}"
    
    db.init_app(app)
    
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix="/")
    
    from .models import Meeting
    
    with app.app_context():
        db.create_all()
    
    return app

def create_database(app):
    if not os.path.exists(DB_NAME):
        with app.app_context():
            db.create_all()
        print('Created Database!')

app = create_app()
create_database(app)
