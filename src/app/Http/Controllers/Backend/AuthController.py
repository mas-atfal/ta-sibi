from flask import render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from ..Controller import Controller
from ....Models.User import User
from .....config.mail import Mail

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
            
    def forgotPassword():
        return render_template("backend/auth/passwords/email.html")
    
    def sendResetPassword():
        email = request.form.get("email")
        
        user = User.query.filter_by(email=email).first()
        
        if not user:
            flash('Email tidak ditemukan', 'danger')
            return redirect(url_for('auth.forgot_password'))
        
        token = user.getResetToken()
        message = Mail.resetPassword(email, token)
        Mail.sendMessage(message)
        
        flash('Silahkan cek email anda', 'success')
        return redirect(url_for('auth.forgot_password'))
    
    def resetVerifiedShow(token):
        return render_template("backend/auth/passwords/reset.html", token=token)
    
    def resetVerifiedPassword(token):
        password = request.form.get("password")
        password_confirmation = request.form.get("password_confirmation")
        
        user = User.verifyResetToken(token)
        
        if not user:
            flash('Token tidak valid', 'danger')
            return redirect(url_for('auth.reset_verified', token=token))
        
        if password != password_confirmation:
            flash('Password tidak cocok', 'danger')
            return redirect(url_for('auth.reset_verified', token=token))
        
        user.setPassword(password, commit=True)
        
        flash('Password berhasil diubah', 'success')
        return redirect(url_for('auth.login'))