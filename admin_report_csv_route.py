
import csv
import io
from flask import Blueprint, request, send_file
from flask_login import login_required, current_user
from ..utils.admin_access_util import get_admin_entities

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/report/csv', methods=['POST'])
@login_required
def download_csv():
    if current_user.role != 'admin':
        return "Access denied", 403

    entity = request.form.get('entity')
    report_type = request.form.get('report_type')
    month = request.form.get('month')
    year = request.form.get('year')

    allowed_entities = get_admin_entities(current_user.username)
    if entity not in allowed_entities:
        return "Unauthorized entity access", 403

    # Dummy report data — replace this with actual query result later
    csv_data = [
        ["Entity", "Report Type", "Month", "Year", "Summary"],
        [entity, report_type, month, year, f"Sample data for {entity} ({report_type})"]
    ]

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerows(csv_data)
    output.seek(0)

    filename = f"{entity}_{report_type}_{month}_{year}.csv"
    return send_file(io.BytesIO(output.getvalue().encode()), mimetype='text/csv', as_attachment=True, download_name=filename)
