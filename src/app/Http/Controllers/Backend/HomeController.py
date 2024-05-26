from flask import render_template
from ..Controller import Controller

class HomeController(Controller):
    def index():
        title = "Home"
        sub_title = {
            "Home": "admin.index",
            "": "#"
        }
        return render_template("backend/home/index.html", title=title, sub_title=sub_title)