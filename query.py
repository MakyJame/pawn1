from models.user import User
from models.customer import Customer

from database import SessionLocal

db = SessionLocal()

user = db.query(Customer).filter(Customer.name == "Minh").first()

print(user.name)
