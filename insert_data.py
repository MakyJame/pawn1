from models.user import User
from models.customer import Customer
from models.pawn import PawnItem

from database import SessionLocal
from datetime import date
db = SessionLocal()
user1 = User(
    username="Minh1",
    email="minh1@gmail.com",
    age=30
)

user2 = User(
    username="Minh2",
    email="minh2@gmail.com",
    age=31
)

item1 = PawnItem(
    date = date(2026,1,1),
    vehicle_num = "50X2-0001",
    pawn_price = 2000000,
    storage = "A8-N1",
    brand = "waveA",

    customer_id = 1
)
item2 = PawnItem(
    date = date(2026,1,2),
    vehicle_num = "50X2-0002",
    pawn_price = 3000000,
    storage = "A8-N2",
    brand = "wave TQ",

    customer_id = 2
)
customer1 = Customer(
    name  = "Doan Van Anh",
    phone = "0789606413"
)
customer2 = Customer(
    name  = "Doan Van Bien",
    phone = "0972973894"
)
db.add(user1)
db.add(user2)

db.add(item1)
db.add(item2)

db.add(customer1)
db.add(customer2)

db.commit()
print("Inserted data!")
