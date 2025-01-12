from flask import render_template
from ...Controller import Controller
from .....Models.Affix import Affix


class AffixController(Controller):
    def index():
        title = "Kata Imbuhan"
        sub_title = sub_title = {
            "Home": "web.index",
            "Kata Imbuhan": "#"
        }
        
        affixes = Affix.query.all()
        
        return render_template("frontend/vocabularies/affixes.html", title=title, sub_title=sub_title, affixes=affixes)