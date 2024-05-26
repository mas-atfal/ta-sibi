from flask import render_template
from ..Controller import Controller

class ArticleController(Controller):
    def index():
        title = "Artikel"
        sub_title = {
            "Home": "admin.index",
            "Artikel": "#"
        }
        
        return render_template("backend/articles/index.html", title=title, sub_title=sub_title)
        
    def create():
        title = "Tambah Artikel"
        sub_title = {
            "Home": "admin.index",
            "Artikel": "admin.articles.index",
            "Tambah": "#"
        }
        
        
        
        return render_template("backend/articles/create.html", title=title, sub_title=sub_title)
    
    def store():
        pass
    
    def edit(id):
        title = "Artikel"
        sub_title = {
            "Home": "admin.index",
            "Artikel": "admin.articles.index",
            "Edit": "#"
        }
        
        return render_template("backend/articles/edit.html", title=title, sub_title=sub_title)
    
    def update(id):
        pass
    
    def destroy(id):
        pass