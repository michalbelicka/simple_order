import pytest
from app import app
from models import db

@pytest.fixture
def client():

    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///:memory:"

    with app.app_context():
        db.drop_all()
        db.create_all()
    
    with app.test_client() as client:
        yield client
    
    with app.app_context():
        db.session.remove()
        db.drop_all()


