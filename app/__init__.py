from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
      import os
    app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET', 'dev-fallback-secret')

    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"

    db.init_app(app)

    from .auth import auth_bp
    from .todo import todo_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(todo_bp)

    with app.app_context():
        db.create_all()

    return app


