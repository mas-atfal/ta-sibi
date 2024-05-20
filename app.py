from flask import Flask
import os

from src import routes
from src.app.Http import Middleware
from src.config.database import create_session_maker

def main() -> Flask:
    app = Flask(__name__, template_folder="src/resources/views", static_url_path="/static", static_folder="public")
    app.secret_key = os.getenv("SECRET_KEY")
    session_maker = create_session_maker(os.getenv("DATABASE_URL"))
    routes.register(app)
    Middleware.register(app, session_maker)
    
    return app

app = main()

if __name__ == "__main__":
    app.run()
