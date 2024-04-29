from flask import render_template
from src.app.Http.Controllers.Controller import Controller

class HomeController(Controller):
    def index():
        title = "Home"
        sub_title = {
            "Home": "web.index", 
            "": "#"
        }
        return render_template("frontend/home/index.html", title=title, sub_title=sub_title)