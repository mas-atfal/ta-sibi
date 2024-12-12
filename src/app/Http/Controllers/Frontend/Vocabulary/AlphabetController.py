from flask import render_template
from ..Controller import Controller
from .....Models.Alphabet import Alphabet

class AlphabetController(Controller):
    def index():
        title = "Abjad"
        sub_title = sub_title = {
            "Home": "web.index",
            "Abjad": "#"
        }
        
        alphabets = Alphabet.query.all()
        
        return render_template("frontend/vocabularies/alphabets/index.html", title=title, sub_title=sub_title, alphabets=alphabets)