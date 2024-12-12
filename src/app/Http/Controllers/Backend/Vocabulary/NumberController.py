from flask import render_template, request, jsonify, url_for
from werkzeug.utils import secure_filename
import os
import app
from slugify import slugify

from ...Controller import Controller
from .....Models.Number import Number

class NumberController(Controller):
    
    global dir
    dir = "backend/vocabularies/numbers/"
    
    def index():
        title = "Angka "
        sub_title = {
            "Home": "admin.index",
            "Angka": "#"
        }
        
        numbers = Number.query.all()
        
        return render_template(dir + "index.html", title=title, sub_title=sub_title, numbers=numbers)
    
    def store():
        try:
            number = Number()
            number.name = request.form.get("name")
            number.slug_name = slugify(request.form.get("name"))
            number.video_link = request.form.get("video_link")
            number.save()
            
            return jsonify({
                "status": True,
                "message": "Angka ditambahkan"
            })
        except Exception as e:
            return jsonify({
                "status": False,
                "message": e
            })
            
    def show(id):
        number = Number.query.get(id)
        
        if not number:
            return jsonify({
                "status": False,
                "message": "Angka tidak ditemukan"
            })
            
        return jsonify({
            "status": True,
            "data": number.jsonResponse()
        })
        
    def update(id):
        number = Number.query.get(id)
                
        if not number:
            return jsonify({
                "status": False,
                "message": "Angka tidak ditemukan"
            })
            
        try:
            number.name = request.form.get("name")
            number.slug_name = slugify(request.form.get("name"))
            number.video_link = request.form.get("video_link")
            number.update()
            
            return jsonify({
                "status": True,
                "message": "Angka diperbarui"   
            })
        except Exception as e:
            return jsonify({
                "status": False,
                "message": str(e)
            })
    
    def destroy(id):
        number = Number.query.get(id)
        
        if not number:
            return jsonify({
                "status": False,
                "message": "Angka tidak ditemukan"
            })
            
        number.delete()
        
        return jsonify({
            "status": True,
            "message": "Angka dihapus"
        })