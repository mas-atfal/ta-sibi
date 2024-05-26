from flask import render_template
from ..Controller import Controller

class DictionaryController(Controller):
    def index():
        title = "Kamus SIBI"
        sub_title = {
            "Home": "admin.index",
            "Kamus SIBI": "#"
        }
        return render_template("backend/dictionaries/index.html", title=title, sub_title=sub_title)