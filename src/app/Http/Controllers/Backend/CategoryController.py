from flask import render_template, request, redirect, url_for, jsonify
from ..Controller import Controller
from ....Models.Category import Category
from slugify import slugify

class CategoryController(Controller):
    def index():
        title = "Kategori"
        sub_title = {
            "Home": "admin.index",
            "Kategori": "#"
        }
        
        categories = Category.getAll()
        
        return render_template("backend/master/categories/index.html", title=title, sub_title=sub_title, categories=categories)
    
    def store():
        try:
            category = Category(name=request.form.get("name"), slug_name=slugify(request.form.get("name")))
            category.save()
            
            return jsonify({
                "status": True,
                "message": "Kategori ditambahkan"
            })
        except Exception as e:
            return jsonify({
                "status": False,
                "message": str(e)
            })
