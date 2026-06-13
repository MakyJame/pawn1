from models.user import User
from repositories.user_repository import(
    get_user_by_email,
    create_user,
    create_pawn
)

def create_user_service(db,username,email,age):
    
    existing_user = get_user_by_email(db,email)

    if existing_user:
        return {"error": "user already exists"}
    if len(username) < 3:
        return {"error": "username at least 3 characters"}
    if age < 18:
        return {"error":"age must be greather than 18"}
    return create_user(db,username,email)

def create_pawn_service(db,date,vehicle_num,pawn_price,storage,brand,customer_id):
    if pawn_price>20000000:
        return {"error":"price is too high"}
    return create_pawn(db,date,vehicle_num,pawn_price,storage,brand,customer_id)
