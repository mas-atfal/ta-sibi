from flask import render_template
from src.app.Http.Controllers.Controller import Controller

class DictionaryController(Controller):
    def index():
        title = "Kamus SIBI"
        sub_title = sub_title = {
            "Home": "web.index",
            "Kamus SIBI": "#"
        }
        return render_template("frontend/dictionaries/index.html", title=title, sub_title=sub_title)