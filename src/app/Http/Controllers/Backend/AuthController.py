from flask import render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from ..Controller import Controller
from ....Models.User import User

class AuthController(Controller):
    def index():
        # password = generate_password_hash('admin123')
        return render_template("backend/auth/login.html")
    
    def doLogin():
        email = request.form.get("email")
        password = request.form.get("password")
        remember = True if request.form.get("remember") else False
        
        user = User.query.filter_by(email=email).first()
        
        if not user or not check_password_hash(user.password, password):
            flash('Please check your login details and try again.', 'danger')
            return redirect(url_for('auth.login'))
        
        login_user(user, remember=remember)
        return redirect(url_for('admin.index'))
    
    def logout():
        try:
            logout_user()
            return jsonify({
                "status": True,
                "message": "Logout success"
            })
        except Exception as e:
            return jsonify({
                "status": False,
                "message": str(e)
            })