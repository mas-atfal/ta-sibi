from flask import render_template, request, jsonify, url_for
from werkzeug.utils import secure_filename
import os
import app
from slugify import slugify

from ...Controller import Controller
from .....Models.Word import Word
from .....Models.Alphabet import Alphabet

class WordController(Controller):
    
    global dir
    dir = "backend/vocabularies/alphabets/words/"
    
    def index():
        alphabet_id = request.args.get("alphabet_id")
        alphabet = Alphabet.query.get(alphabet_id)

        title = "Kata Dasar " + alphabet.name
        sub_title = {
            "Home": "admin.index",
            "Kata Dasar": "#"
        }
        
        words = Word.query.filter_by(alphabet_id=alphabet_id).all()
        
        return render_template(dir + "index.html", title=title, sub_title=sub_title, words=words)
    
    def store():
        try:
            word = Word()
            word.name = request.form.get("name")
            word.slug_name = slugify(request.form.get("name"))
            word.video_link = request.form.get("video_link")
            word.alphabet_id = request.form.get("alphabet_id")
            word.save()
            
            return jsonify({
                "status": True,
                "message": "Kata Dasar ditambahkan"
            })
        except Exception as e:
            return jsonify({
                "status": False,
                "message": e
            })
            
    def show(id):
        word = Word.query.get(id)
        
        if not word:
            return jsonify({
                "status": False,
                "message": "Kata Dasar tidak ditemukan"
            })
            
        return jsonify({
            "status": True,
            "data": word.jsonResponse()
        })
        
    def update(id):
        word = Word.query.get(id)
                
        if not word:
            return jsonify({
                "status": False,
                "message": "Kata Dasar tidak ditemukan"
            })
            
        try:
            word.name = request.form.get("name")
            word.slug_name = slugify(request.form.get("name"))
            word.video_link = request.form.get("video_link")
            word.update()
            
            return jsonify({
                "status": True,
                "message": "Kata Dasar diperbarui"   
            })
        except Exception as e:
            return jsonify({
                "status": False,
                "message": str(e)
            })
    
    def destroy(id):
        word = Word.query.get(id)
        
        if not word:
            return jsonify({
                "status": False,
                "message": "Kata Dasar tidak ditemukan"
            })
            
        word.delete()
        
        return jsonify({
            "status": True,
            "message": "Kata Dasar dihapus"
        })