from flask import render_template
from ..Controller import Controller
from ....Models.Article import Article

class ArticleController(Controller):
    def index():
        title = "Artikel"
        sub_title = sub_title = {
            "Home": "web.index",
            "Artikel": "#"
        }
        
        articles = Article.query.all()
        
        return render_template("frontend/articles/index.html", title=title, sub_title=sub_title, articles=articles)
    
    def show(slug):
        title = "Artikel"
        sub_title = sub_title = {
            "Home": "web.index",
            "Artikel": "#"
        }
        
        article = Article.query.filter_by(slug_title=slug).first()
        
        return render_template("frontend/articles/show.html", title=title, sub_title=sub_title, article=article)