from flask import render_template, request, redirect, url_for, jsonify
from ..Controller import Controller
# from ....Models.Category import Category
from slugify import slugify

class SingkatanController(Controller):
    def index():
        title = "Singkatan"
        sub_title = {
            "Home": "admin.index",
            "Singkatan": "#"
        }
        
        # categories = Category.query.all()
        
        return render_template("backend/singkatan/index.html", title=title, sub_title=sub_title)