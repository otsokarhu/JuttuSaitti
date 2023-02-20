import os
from flask import request, session, abort
from db import db
from sqlalchemy.sql import text


def add_contact_request(name, email, message):
    sql = text(
        "INSERT INTO contact (name, email, message) VALUES (:name, :email, :message)")
    db.session.execute(sql, {"name": name, "email": email, "message": message})
    db.session.commit()


def get_contact_requests():
    sql = text("SELECT id, name, email, message FROM contact")
    result = db.session.execute(sql)
    return result.fetchall()
