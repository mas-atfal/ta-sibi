from flask import render_template
from ...Controller import Controller
from .....Models.Alphabet import Alphabet

class AlphabetController(Controller):
    def index():
        title = "Abjad"
        sub_title = sub_title = {
            "Home": "web.index",
            "Abjad": "#"
        }
        
        alphabets = Alphabet.query.all()
        
        return render_template("frontend/vocabularies/alphabets.html", title=title, sub_title=sub_title, alphabets=alphabets)
    
    def show(alphabet_id):
        title = "Abjad"
        sub_title = sub_title = {
            "Home": "web.index",
            "Abjad": "#"
        }
        
        alphabet = Alphabet.query.get(alphabet_id)
        
        return render_template("frontend/vocabularies/alphabets/show.html", title=title, sub_title=sub_title, alphabet=alphabet)