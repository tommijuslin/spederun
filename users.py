import os
from db import db
from flask import session, abort, request
from werkzeug.security import check_password_hash, generate_password_hash

def login(username, password):
    sql = "SELECT id, password, role FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        return False
    else:
        if check_password_hash(user.password, password):
            session["user_id"] = user.id
            session["username"] = username
            session["csrf_token"] = os.urandom(16).hex()
            session["user_role"] = user.role
            return True
        else:
            return False

def register(username, password):
    hash_value = generate_password_hash(password)
    try:
        sql = "INSERT INTO users (username, password, role) VALUES (:username, :password, 0)"
        db.session.execute(sql, {"username":username, "password":hash_value})
        db.session.commit()
    except:
        return False
    return login(username, password)

def get_username(username):
    sql = "SELECT username FROM users WHERE UPPER(username)=UPPER(:username)"
    return db.session.execute(sql, {"username":username}).fetchone()

def get_user(id):
    sql = "SELECT id, username FROM users WHERE id=:id"
    return db.session.execute(sql, {"id":id}).fetchone()

def check_csrf(token):
    if session["csrf_token"] != token:
        abort(403)

def require_role(role):
    return session.get("user_role", 0) == role
