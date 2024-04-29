from flask import render_template
from src.app.Http.Controllers.Controller import Controller

class LearningController(Controller):
    def index():
        title = "Home"
        sub_title = {
            "Home": "web.index", 
            "Learning": "#"
        }
        return render_template("frontend/learning/index.html", title=title, sub_title=sub_title)