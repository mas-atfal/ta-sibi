from flask import render_template
from src.app.Http.Controllers.Controller import Controller

class ArticleController(Controller):
    def index():
        title = "Artikel"
        sub_title = sub_title = {
            "Home": "web.index",
            "Artikel": "#"
        }
        return render_template("frontend/articles/index.html", title=title, sub_title=sub_title)