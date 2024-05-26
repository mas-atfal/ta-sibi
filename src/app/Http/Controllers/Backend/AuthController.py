from flask import render_template
from src.app.Http.Controllers.Controller import Controller

class AuthController(Controller):
    def index():
        return render_template("backend/auth/login.html")
    
    def doLogin():
        pass
    
    def logout():
        pass