from flask import render_template
from src.app.Http.Controllers.Controller import Controller

from ....Models.Alphabet import Alphabet
from ....Models.Article import Article

class HomeController(Controller):
    def index():
        title = "Home"
        sub_title = {
            "Home": "web.index", 
            "": "#"
        }
        
        alphabets = Alphabet.query.limit(6).all()
        articles = Article.query.limit(6).all()
        
        return render_template("frontend/home/index.html", title=title, sub_title=sub_title, alphabets=alphabets, articles=articles)