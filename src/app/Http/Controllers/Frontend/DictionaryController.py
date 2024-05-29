from flask import render_template
from ..Controller import Controller
from ....Models.Dictionary import Dictionary

class DictionaryController(Controller):
    def index():
        title = "Kamus SIBI"
        sub_title = sub_title = {
            "Home": "web.index",
            "Kamus SIBI": "#"
        }
        
        dictionaries = Dictionary.query.all()
        
        return render_template("frontend/dictionaries/index.html", title=title, sub_title=sub_title, dictionaries=dictionaries)