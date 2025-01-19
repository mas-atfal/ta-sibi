from flask import render_template, request, jsonify, url_for
from werkzeug.utils import secure_filename
import os
import app
from slugify import slugify

from ...Controller import Controller
from .....Models.Alphabet import Alphabet

class AlphabetController(Controller):
    
    def allowed_file(filename):
        ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    
    def index():
        title = "Abjad"
        sub_title = {
            "Home": "admin.index",
            "Abjad": "#"
        }
        
        alphabets = Alphabet.query.all()
        
        return render_template("backend/vocabularies/alphabets/index.html", title=title, sub_title=sub_title, alphabets=alphabets)
    
    def store():
        try:
            alphabet = Alphabet()
            alphabet.name = request.form.get("name")
            alphabet.slug_name = slugify(request.form.get("name"))
            alphabet.description = request.form.get("description")
            
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
            if file and AlphabetController.allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(os.getenv("FILESYSTEM_DRIVER")+'/alphabets', filename))
            
            alphabet.image = filename
            alphabet.save()
            
            return jsonify({
                "status": True,
                "message": "Abjad ditambahkan"
            })
        except Exception as e:
            return jsonify({
                "status": False,
                "message": e.__str__()
            })
            
    def show(id):
        alphabet = Alphabet.query.get(id)
        
        if not alphabet:
            return jsonify({
                "status": False,
                "message": "Abjad tidak ditemukan"
            })
            
        return jsonify({
            "status": True,
            "data": alphabet.jsonResponse()
        })
        
    def update(id):
        alphabet = Alphabet.query.get(id)
                
        if not alphabet:
            return jsonify({
                "status": False,
                "message": "Abjad tidak ditemukan"
            })
            
        try:
            alphabet.name = request.form.get("name")
            alphabet.slug_name = slugify(request.form.get("name"))
            alphabet.description = request.form.get("description")
            
            filename = alphabet.image
            
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
                if file and AlphabetController.allowed_file(file.filename):
                    os.remove(os.getenv("FILESYSTEM_DRIVER")+'/alphabets/'+alphabet.image)
                    filename = secure_filename(file.filename)
                    file.save(os.path.join(os.getenv("FILESYSTEM_DRIVER")+'/alphabets', filename))
            
            alphabet.image = filename
            alphabet.update()
            
            return jsonify({
                "status": True,
                "message": "Abjad diperbarui"   
            })
        except Exception as e:
            return jsonify({
                "status": False,
                "message": str(e)
            })
    
    def destroy(id):
        alphabet = Alphabet.query.get(id)
        
        if not alphabet:
            return jsonify({
                "status": False,
                "message": "Abjad tidak ditemukan"
            })
            
        os.remove(os.getenv("FILESYSTEM_DRIVER")+'/alphabets/'+alphabet.image)
        alphabet.delete()
        
        return jsonify({
            "status": True,
            "message": "Abjad dihapus"
        })