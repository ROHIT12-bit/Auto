from pymongo import MongoClient
from config import Config

client = MongoClient(Config.MONGO_URI)
db = client[Config.DB_NAME]

approved_users_col = db["approved_users"]
admin_col = db["admins"]

def is_admin(user_id):
    return admin_col.find_one({"user_id": user_id}) is not None

def add_admin(user_id):
    if not is_admin(user_id):
        admin_col.insert_one({"user_id": user_id})

def remove_admin(user_id):
    admin_col.delete_one({"user_id": user_id})

def get_all_admins():
    return [x["user_id"] for x in admin_col.find()]

def approve_user(chat_id, user_id):
    approved_users_col.update_one(
        {"chat_id": chat_id},
        {"$addToSet": {"approved": user_id}},
        upsert=True
    )

def is_user_approved(chat_id, user_id):
    chat_data = approved_users_col.find_one({"chat_id": chat_id})
    return chat_data and user_id in chat_data.get("approved", [])

def get_total_approved():
    total = 0
    for chat in approved_users_col.find():
        total += len(chat.get("approved", []))
    return total
