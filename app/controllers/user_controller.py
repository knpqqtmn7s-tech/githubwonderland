from data.fake_db import users_db

def get_users():
    return users_db

def create_user(user_data):
    new_user = {
        "userId": len(users_db) + 1,
        "username": user_data.username,
        "email": user_data.email
    }
    users_db.append(new_user)
    return new_user
