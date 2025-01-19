from flask import render_template
from ...Controller import Controller
from .....Models.Alphabet import Alphabet
from .....Models.Word import Word

class AlphabetController(Controller):
    def index():
        title = "Abjad"
        sub_title = sub_title = {
            "Home": "web.index",
            "Abjad": "#"
        }
        
        alphabets = Alphabet.query.all()
        
        return render_template("frontend/vocabularies/alphabets.html", title=title, sub_title=sub_title, alphabets=alphabets)
    
    def show(id):
        title = "Abjad"
        sub_title = sub_title = {
            "Home": "web.index",
            "Abjad": "#"
        }
        
        words = Word.query.filter_by(alphabet_id=id).all()
        
        return render_template("frontend/vocabularies/show_alphabet.html", title=title, sub_title=sub_title, words=words)