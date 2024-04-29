from flask import Blueprint, g

bpApi = Blueprint("api", __name__, url_prefix="/api")

@bpApi.route("/")
def index():
    return "Hello, World!"