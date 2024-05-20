from flask import render_template
from pydantic import TypeAdapter
from src.app.Http.Controllers.Controller import Controller
from src.app.Models.User import User as UserModel
from src.app.Schemas.UserSchema import User as UserSchema

from sqlalchemy import select

class ArticleController(Controller[UserModel]):
    def index():
        title = "Artikel"
        sub_title = {
            "Home": "admin.index",
            "Artikel": "#"
        }
        
        return render_template("backend/articles/index.html", title=title, sub_title=sub_title)
    
    def json(self) -> list[UserSchema]:
        stmt = select(UserModel)
        result = self.session.scalars(stmt.order_by(UserModel.id)).fetchall()
        return TypeAdapter(list[UserSchema]).validate_python(result)
        
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