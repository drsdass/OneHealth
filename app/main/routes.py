from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from app.utils.admin_access_util import get_admin_entities

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return redirect(url_for('auth.login'))

@main_bp.route('/dashboard')
@login_required
def dashboard():
    if current_user.role == 'admin':
        entities = get_admin_entities(current_user.username)
        return render_template('main/admin_dashboard.html', user=current_user, entities=entities)
    elif current_user.role == 'provider':
        return render_template('main/provider_dashboard.html', user=current_user)
    elif current_user.role == 'patient':
        return render_template('main/patient_dashboard.html', user=current_user)
    elif current_user.role == 'bizdev':
        return render_template('main/bizdev_dashboard.html', user=current_user)
    else:
        return "Unauthorized role", 403