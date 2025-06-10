
from flask import Blueprint, request, render_template
from flask_login import login_required, current_user
from ..utils.admin_access_util import get_admin_entities

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/report', methods=['POST'])
@login_required
def generate_report():
    if current_user.role != 'admin':
        return "Access denied", 403

    entity = request.form.get('entity')
    report_type = request.form.get('report_type')
    month = request.form.get('month')
    year = request.form.get('year')

    allowed_entities = get_admin_entities(current_user.username)
    if entity not in allowed_entities:
        return "Unauthorized entity access", 403

    # Placeholder report generation logic
    report_data = {
        "entity": entity,
        "report_type": report_type,
        "month": month,
        "year": year,
        "details": f"Showing dummy {report_type} report for {entity}, {month}/{year}."
    }

    return render_template('main/admin_report.html', report=report_data)
