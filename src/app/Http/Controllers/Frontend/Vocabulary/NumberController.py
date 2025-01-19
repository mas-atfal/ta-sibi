from flask import render_template
from ...Controller import Controller
from .....Models.Number import Number


class NumberController(Controller):
    def index():
        title = "Angka"
        sub_title = sub_title = {
            "Home": "web.index",
            "Angka": "#"
        }
        
        numbers = Number.query.all()
        
        return render_template("frontend/vocabularies/numbers.html", title=title, sub_title=sub_title, numbers=numbers)