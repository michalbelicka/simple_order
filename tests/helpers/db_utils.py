from models import db, Order
from app import app

def get_order_from_db(order_id):
    
    with app.app_context():
        return db.session.get(Order, order_id)

    