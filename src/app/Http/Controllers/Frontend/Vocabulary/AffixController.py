from flask import render_template, request
from ...Controller import Controller
from .....Models.Affix import Affix


class AffixController(Controller):
    def index():
        type = request.args.get("type")
        
        title = "Kata Imbuhan"
        sub_title = sub_title = {
            "Home": "web.index",
            "Kata Imbuhan": "#"
        }
        
        affixes = Affix.query.filter_by(type=type).all()
        
        return render_template("frontend/vocabularies/affixes.html", title=title, sub_title=sub_title, affixes=affixes)