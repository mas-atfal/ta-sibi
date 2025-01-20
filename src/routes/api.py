from flask import Blueprint, g, jsonify, request
from src.app.Models.Singkatan import Singkatan
from sqlalchemy import func

bpApi = Blueprint("api", __name__, url_prefix="/api")

@bpApi.route("/")
def index():
    return "Hello, World!"


@bpApi.route("/singkatan")
def singkatan():
    q = request.args.get('q', None)
    singkatan = Singkatan.query.filter(func.upper(
        Singkatan.singkatan) == str(q).upper()).all()

    if not singkatan:
        return jsonify({
            "status": False,
            "message": "Singkatan tidak ditemukan"
        })
    thejson = [skt.jsonResponse() for skt in singkatan]
    return jsonify({
        "status": True,
        "data": thejson
    })
