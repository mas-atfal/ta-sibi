from flask import Flask
from datetime import datetime

from .web import bpWeb, bpAuth, bpAdmin
from .api import bpApi

def register(app: Flask) -> None:
    # Context
    @app.context_processor
    def inject_now():
        return {'now': datetime.utcnow()}
    # Web
    app.register_blueprint(bpWeb)
    app.register_blueprint(bpAuth)
    
    # Blueprint admin
    app.register_blueprint(bpAdmin)
    
    # Api
    app.register_blueprint(bpApi)
    