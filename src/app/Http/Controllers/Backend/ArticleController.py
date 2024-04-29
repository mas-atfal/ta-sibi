from flask import render_template
from src.app.Http.Controllers.Controller import Controller

class ArticleController(Controller):
    def index():
        title = "Artikel"
        sub_title = {
            "Home": "admin.index",
            "Artikel": "#"
        }
        return render_template("backend/articles/index.html", title=title, sub_title=sub_title)