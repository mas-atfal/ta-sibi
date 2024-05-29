from flask import render_template, url_for, jsonify, request
from ..Controller import Controller
from werkzeug.utils import secure_filename
import os
import app
from slugify import slugify

from ....Models.Category import Category
from ....Models.Article import Article

class ArticleController(Controller):
    def allowed_file(filename):
        ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    
    def index():
        title = "Artikel"
        sub_title = {
            "Home": "admin.index",
            "Artikel": "#"
        }
        
        articles = Article.query.all()
        
        return render_template("backend/articles/index.html", title=title, sub_title=sub_title, articles=articles)
        
    def create():
        title = "Tambah Artikel"
        sub_title = {
            "Home": "admin.index",
            "Artikel": "admin.articles.index",
            "Tambah": "#"
        }
        
        categories = Category.query.all()
        
        return render_template("backend/articles/create.html", title=title, sub_title=sub_title, categories=categories)
    
    def store():
        try:
            article = Article()
            article.user_id = 1
            article.category_id = request.form.get("category_id")
            article.title = request.form.get("title")
            article.slug_title = slugify(request.form.get("title"))
            article.content = request.form.get("content")
            article.status = request.form.get("status")
            
            # check if the post request has the file part
            if 'image' not in request.files:
                return jsonify({
                    "status": False,
                    "message": "No file part"
                })
            file = request.files['image']
            # if user does not select file, browser also
            # submit a empty part without filename
            if file.filename == '':
                return jsonify({
                    "status": False,
                    "message": "No selected file"
                })
            if file and ArticleController.allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(os.getenv("FILESYSTEM_DRIVER")+'/articles', filename))
            
            article.image = filename
            
            article.save()
            
            return jsonify({
                "status": True,
                "message": "Artikel ditambahkan"
            })
        except Exception as e:
            return jsonify({
                "status": False,
                "message": str(e)
            })
    
    def edit(id):
        title = "Artikel"
        sub_title = {
            "Home": "admin.index",
            "Artikel": "admin.articles.index",
            "Edit": "#"
        }
        
        article = Article.query.get(id)
        categories = Category.query.all()
        
        return render_template("backend/articles/edit.html", title=title, sub_title=sub_title, article=article, categories=categories)
    
    def update(id):
        article = Article.query.get(id)
        
        if not article:
            return jsonify({
                "status": False,
                "message": "Artikel tidak ditemukan"
            })

        try:
            article.user_id = 1
            article.category_id = request.form.get("category_id")
            article.title = request.form.get("title")
            article.slug_title = slugify(request.form.get("title"))
            article.content = request.form.get("content")
            article.status = request.form.get("status")
            
            filename = article.image
            
            # check if the post request has the file part
            if 'image' not in request.files:
                return jsonify({
                    "status": False,
                    "message": "No file part"
                })
            # if user does not select file, browser also
            # submit a empty part without filename
            if request.files['image']:
                file = request.files['image']
                if file.filename == '':
                    return jsonify({
                        "status": False,
                        "message": "No selected file"
                    })
                if file and ArticleController.allowed_file(file.filename):
                    os.remove(os.getenv("FILESYSTEM_DRIVER")+'/articles/'+article.image)
                    
                    filename = secure_filename(file.filename)
                    file.save(os.path.join(os.getenv("FILESYSTEM_DRIVER")+'/articles', filename))
            
            article.image = filename
            
            article.update()
            
            return jsonify({
                "status": True,
                "message": "Artikel diperbarui"
            })
        except Exception as e:
            return jsonify({
                "status": False,
                "message": str(e)
            })
    
    def destroy(id):
        article = Article.query.get(id)
        
        if not article:
            return jsonify({
                "status": False,
                "message": "Artikel tidak ditemukan"
            })
            
        os.remove(os.getenv("FILESYSTEM_DRIVER")+'/articles/'+article.image)
        article.delete()
        
        return jsonify({
            "status": True,
            "message": "Artikel dihapus"
        })