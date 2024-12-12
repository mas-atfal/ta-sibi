from flask import render_template, request, jsonify, url_for
from werkzeug.utils import secure_filename
import os
import app
from slugify import slugify

from ...Controller import Controller
from .....Models.Affix import Affix

class AffixController(Controller):
    
    global dir
    dir = "backend/vocabularies/affixes/"
    
    def index():
        title = "Kata Imbuhan "
        sub_title = {
            "Home": "admin.index",
            "Kata Imbuhan": "#"
        }
        
        affixes = Affix.query.all()
        
        return render_template(dir + "index.html", title=title, sub_title=sub_title, affixes=affixes)
    
    def store():
        try:
            affix = Affix()
            affix.name = request.form.get("name")
            affix.slug_name = slugify(request.form.get("name"))
            affix.video_link = request.form.get("video_link")
            affix.type = request.form.get("type")
            affix.save()
            
            return jsonify({
                "status": True,
                "message": "Kata Imbuhan ditambahkan"
            })
        except Exception as e:
            return jsonify({
                "status": False,
                "message": e
            })
            
    def show(id):
        affix = Affix.query.get(id)
        
        if not affix:
            return jsonify({
                "status": False,
                "message": "Kata Imbuhan tidak ditemukan"
            })
            
        return jsonify({
            "status": True,
            "data": affix.jsonResponse()
        })
        
    def update(id):
        affix = Affix.query.get(id)
                
        if not affix:
            return jsonify({
                "status": False,
                "message": "Kata Imbuhan tidak ditemukan"
            })
            
        try:
            affix.name = request.form.get("name")
            affix.slug_name = slugify(request.form.get("name"))
            affix.video_link = request.form.get("video_link")
            affix.type = request.form.get("type")
            affix.update()
            
            return jsonify({
                "status": True,
                "message": "Kata Imbuhan diperbarui"   
            })
        except Exception as e:
            return jsonify({
                "status": False,
                "message": str(e)
            })
    
    def destroy(id):
        affix = Affix.query.get(id)
        
        if not affix:
            return jsonify({
                "status": False,
                "message": "Kata Imbuhan tidak ditemukan"
            })
            
        affix.delete()
        
        return jsonify({
            "status": True,
            "message": "Kata Imbuhan dihapus"
        })