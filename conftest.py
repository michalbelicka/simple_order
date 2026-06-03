import pytest
from app import app
from models import db, Order
from pathlib import Path

# @pytest.fixture(scope="module", autouse=True)
# def clear_db():

#     with app.app_context():
#         db.session.query(Order).delete()
#         db.session.commit()

BASE_DIR = Path(__file__).resolve().parent
db_path = BASE_DIR / "tests" / "test.db"

@pytest.fixture
def client():

    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"

    with app.app_context():
        db.drop_all()
        db.create_all()
    
    with app.test_client() as client:
        yield client
    
    with app.app_context():
        db.session.remove()
        db.drop_all()


