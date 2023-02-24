import os
from flask import request, session, abort
from db import db
import secrets
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.sql import text


def register(username, password, admin):
    hash_value = generate_password_hash(password)

    sql = text(
        "INSERT INTO users (username, password, admin) VALUES (:username, :password, :admin)")
    db.session.execute(
        sql, {"username": username, "password": hash_value, "admin": admin})
    db.session.commit()

    return True


def login(username, password):
    sql = text("SELECT id, password, admin FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username": username})
    user = result.fetchone()
    if not user:
        return False
    else:
        hash_value = user[1]
        if not check_password_hash(hash_value, password):
            return False
        session["user_id"] = user[0]
        session["user_name"] = username
        session["csrf_token"] = secrets.token_hex(16)
        session["admin"] = user[2]
        print(user)
        return True


def get_user_id():
    return session.get("user_id", 0)


def get_username(id):
    sql = text("SELECT username FROM users WHERE id=:id")
    result = db.session.execute(sql, {"id": id})
    return result.fetchone()[0]


def get_user_count():
    sql = text("SELECT COUNT(*) FROM users")
    result = db.session.execute(sql)
    return result.fetchone()[0]


def logout():
    del session["user_id"]
    del session["csrf_token"]
    del session["user_name"]
