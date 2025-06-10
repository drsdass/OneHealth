
from flask import Blueprint, render_template
from flask_login import login_required, current_user

main_bp = Blueprint('main', __name__)

@main_bp.route('/dashboard')
@login_required
def dashboard():
    if current_user.role == 'admin':
        return render_template('main/admin_dashboard.html', user=current_user)
    elif current_user.role == 'provider':
        return render_template('main/provider_dashboard.html', user=current_user)
    elif current_user.role == 'patient':
        return render_template('main/patient_dashboard.html', user=current_user)
    elif current_user.role == 'bizdev':
        return render_template('main/bizdev_dashboard.html', user=current_user)
    else:
        return "Unauthorized role", 403
