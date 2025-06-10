from flask import Blueprint, render_template
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route("/dashboard")
@login_required
def dashboard():
    if current_user.role == 'admin':
        return "Admin Dashboard"
    return "User Dashboard"
