from flask import render_template, request, jsonify, url_for
from werkzeug.utils import secure_filename
import os
import app
from slugify import slugify

from ..Controller import Controller
from ....Models.Dictionary import Dictionary

class DictionaryController(Controller):
    
    def allowed_file(filename):
        ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    
    def index():
        title = "Kamus SIBI"
        sub_title = {
            "Home": "admin.index",
            "Kamus SIBI": "#"
        }
        
        dictionaries = Dictionary.query.all()
        
        return render_template("backend/dictionaries/index.html", title=title, sub_title=sub_title, dictionaries=dictionaries)
    
    def store():
        try:
            dictionary = Dictionary()
            dictionary.name = request.form.get("name")
            dictionary.slug_name = slugify(request.form.get("name"))
            dictionary.description = request.form.get("description")
            
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
            if file and DictionaryController.allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(os.getenv("FILESYSTEM_DRIVER")+'/dictionaries', filename))
            
            dictionary.image = filename
            dictionary.save()
            
            return jsonify({
                "status": True,
                "message": "Kamus ditambahkan"
            })
        except Exception as e:
            return jsonify({
                "status": False,
                "message": str(e)
            })
            
    def show(id):
        dictionary = Dictionary.query.get(id)
        
        if not dictionary:
            return jsonify({
                "status": False,
                "message": "Kamus tidak ditemukan"
            })
            
        return jsonify({
            "status": True,
            "data": dictionary.jsonResponse()
        })
        
    def update(id):
        dictionary = Dictionary.query.get(id)
                
        if not dictionary:
            return jsonify({
                "status": False,
                "message": "Kamus tidak ditemukan"
            })
            
        try:
            dictionary.name = request.form.get("name")
            dictionary.slug_name = slugify(request.form.get("name"))
            dictionary.description = request.form.get("description")
            
            filename = dictionary.image
            
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
                if file and DictionaryController.allowed_file(file.filename):
                    os.remove(os.getenv("FILESYSTEM_DRIVER")+'/dictionaries/'+dictionary.image)
                    filename = secure_filename(file.filename)
                    file.save(os.path.join(os.getenv("FILESYSTEM_DRIVER")+'/dictionaries', filename))
            
            dictionary.image = filename
            dictionary.update()
            
            return jsonify({
                "status": True,
                "message": "Kamus diperbarui"   
            })
        except Exception as e:
            return jsonify({
                "status": False,
                "message": str(e)
            })
    
    def destroy(id):
        dictionary = Dictionary.query.get(id)
        
        if not dictionary:
            return jsonify({
                "status": False,
                "message": "Kamus tidak ditemukan"
            })
            
        os.remove(os.getenv("FILESYSTEM_DRIVER")+'/dictionaries/'+dictionary.image)
        dictionary.delete()
        
        return jsonify({
            "status": True,
            "message": "Kamus dihapus"
        })