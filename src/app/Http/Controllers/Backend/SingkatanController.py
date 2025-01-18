from flask import render_template, request, redirect, url_for, jsonify
from ..Controller import Controller
from ....Models.Singkatan import Singkatan
from slugify import slugify

class SingkatanController(Controller):
    def index():
        title = "Singkatan"
        sub_title = {
            "Home": "admin.index",
            "Singkatan": "#"
        }
        
        singkatans = Singkatan.query.all()
        
        return render_template("backend/singkatan/index.html", title=title, sub_title=sub_title, singkatans=singkatans)
    
    def store():
        try:
            singkatan = Singkatan()
            singkatan.singkatan = request.form.get("singkatan")
            singkatan.kepanjangan = request.form.get("kepanjangan")
            singkatan.save()
            
            return jsonify({
                "status": True,
                "message": "Singkatan ditambahkan"
            })
        except Exception as e:
            return jsonify({
                "status": False,
                "message": e
            })
            
    def show(id):
        singkatan = Singkatan.query.get(id)
        
        if not singkatan:
            return jsonify({
                "status": False,
                "message": "Singkatan tidak ditemukan"
            })
            
        return jsonify({
            "status": True,
            "data": singkatan.jsonResponse()
        })
        
    def update(id):
        singkatan = Singkatan.query.get(id)
                
        if not singkatan:
            return jsonify({
                "status": False,
                "message": "Singkatan tidak ditemukan"
            })
            
        try:
            singkatan.name = request.form.get("name")
            singkatan.singkatan = request.form.get("singkatan")
            singkatan.kepanjangan = request.form.get("kepanjangan")
            singkatan.update()
            
            return jsonify({
                "status": True,
                "message": "Singkatan diperbarui"   
            })
        except Exception as e:
            return jsonify({
                "status": False,
                "message": str(e)
            })
    
    def destroy(id):
        singkatan = Singkatan.query.get(id)
        
        if not singkatan:
            return jsonify({
                "status": False,
                "message": "Singkatan tidak ditemukan"
            })
            
        singkatan.delete()
        
        return jsonify({
            "status": True,
            "message": "Singkatan dihapus"
        })