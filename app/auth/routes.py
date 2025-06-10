
from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from werkzeug.security import check_password_hash
from .. import login_manager
from flask_login import login_user, logout_user, login_required, UserMixin

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

class User(UserMixin):
    def __init__(self, id):
        self.id = id
        self.name = id
        self.password = 'pbkdf2:sha256:150000$hashedpassword'

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        user = User(username)
        login_user(user)
        return redirect(url_for('main.dashboard'))
    return render_template('auth/login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
