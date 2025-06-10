
from app import create_app
from app.models import db, User

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    admin = User(username='admin', role='admin')
    admin.set_password('adminpass')

    provider = User(username='drsmith', role='provider')
    provider.set_password('providerpass')

    patient = User(username='johndoe', role='patient')
    patient.set_password('patientpass')

    db.session.add(admin)
    db.session.add(provider)
    db.session.add(patient)
    db.session.commit()

    print("Database initialized and users created.")
