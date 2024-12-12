from flask import render_template
from ...Controller import Controller
from .....Models.Alphabet import Alphabet
from .....Models.Affix import Affix
from .....Models.Number import Number

class VocabularyController(Controller):
    def index():
        title = "Abjad"
        sub_title = sub_title = {
            "Home": "web.index",
            "Abjad": "#"
        }
        
        alphabets = Alphabet.query.all()
        affixes = Affix.query.all()
        numbers = Number.query.all()
        
        return render_template("frontend/vocabularies/index.html", title=title, sub_title=sub_title, alphabets=alphabets, affixes=affixes, numbers=numbers)