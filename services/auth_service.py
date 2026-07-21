from repositories.auth_repository import save_user_in_database, get_user_detail
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import create_access_token

def register_service(username, password):
    user_detail = get_user_detail(username)
    if user_detail:
        return "username not available, Try another one"
    hash_pass = generate_password_hash(password)
    save_user_in_database(username, hash_pass)
    return None

def login_service(username, password):
    user_detail = get_user_detail(username)
    if not user_detail:
        return None, "user not exists, check username and try again"
    if check_password_hash(user_detail[1], password):
        token = create_access_token(identity=username)
        return token, None
    else:
        return None, "check password and try again"
    