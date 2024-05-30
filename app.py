from flask import Flask
import os

from src import routes
from src.app.Http import Middleware
from src.config.database import db
from src.app.Models.User import User
from flask_login import LoginManager

def main() -> Flask:
    app = Flask(__name__, template_folder="src/resources/views", static_url_path="/static", static_folder="public")
    
    app.secret_key = os.getenv("SECRET_KEY")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
    
    app.config['UPLOAD_FOLDER'] = 'public/storage'
    
    db.init_app(app)
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    
    routes.register(app)
    
    return app

app = main()

if __name__ == "__main__":
    app.run()
