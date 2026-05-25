import pytest
from app import app
from models import db, Order

@pytest.fixture(scope="module", autouse=True)
def clear_db():

    with app.app_context():
        db.session.query(Order).delete()
        db.session.commit()

