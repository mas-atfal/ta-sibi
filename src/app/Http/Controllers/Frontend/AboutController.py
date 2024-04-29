from flask import render_template
from src.app.Http.Controllers.Controller import Controller

class AboutController(Controller):
    def index():
        title = "Tentang"
        sub_title = sub_title = {
            "Home": "web.index",
            "Tentang": "#"
        }
        return render_template("frontend/about/index.html", title=title, sub_title=sub_title)