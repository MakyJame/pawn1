from models.user import User
from models.pawn import PawnItem
from models.customer import Customer
from datetime import date

def get_all_user(db):
	return db.query(User).all()

def get_all_customer(db):
    return db.query(PawnItem).all()

def create_user(db,username,email,age):
	new_user=User(
		username=username,
		email=email,
        age=age
	)
	
	db.add(new_user)	
	db.commit()
	db.refresh(new_user)
	return new_user

def get_user_by_email(db,email):
    return db.query(User).filter(User.email == email).first()

def delete_user(db,user_id):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None
    
    db.delete(user)
    db.commit()
    return user

def get_all_pawn(db):
    return db.query(PawnItem).all()

def create_pawn(db,date,vehicle_num,pawn_price,storage,brand,customer_id):
    new_pawn=PawnItem(
        date=date,
        vehicle_num=vehicle_num,
        pawn_price=pawn_price,
        storage=storage,
        brand=brand,
        customer_id=customer_id
    )
    
    db.add(new_pawn)
    db.commit()
    db.refresh(new_pawn)
    return new_pawn

def get_all_customer(db):
    return db.query(Customer).all()

def create_customer(db,name,phone):
    new_customer=Customer(
        name=name,
        phone=phone
    )
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return new_customer
