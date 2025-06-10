
from flask import Blueprint, render_template
from flask_login import login_required, current_user

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/panel')
@login_required
def panel():
    if current_user.role != 'admin':
        return "Access Denied", 403
    return render_template('admin/panel.html', user=current_user)
