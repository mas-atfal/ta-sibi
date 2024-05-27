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
        
        categories = Category.query.all()
        
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
            
    def show(id):
        category = Category.query.get(id)
        
        if not category:
            return jsonify({
                "status": False,
                "message": "Kategori tidak ditemukan"
            })
            
        return jsonify({
            "status": True,
            "data": category.jsonResponse()
        })
        
    def update(id):
        category = Category.query.get(id)
        
        if not category:
            return jsonify({
                "status": False,
                "message": "Kategori tidak ditemukan"
            })
            
        try:
            category.name = request.form.get("name")
            category.slug_name = slugify(request.form.get("name"))
            category.update()
            
            return jsonify({
                "status": True,
                "message": "Kategori diperbarui"
            })
        except Exception as e:
            return jsonify({
                "status": False,
                "message": str(e)
            })
            
    def destroy(id):
        category = Category.query.get(id)
        
        if not category:
            return jsonify({
                "status": False,
                "message": "Kategori tidak ditemukan"
            })
            
        category.delete()
        
        return jsonify({
            "status": True,
            "message": "Kategori dihapus"
        })
