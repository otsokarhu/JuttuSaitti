import os
from flask import request, session, abort
from db import db
import secrets
from sqlalchemy.sql import text


def add_post(title, content):
    sql = text("INSERT INTO posts (title, content) VALUES (:title, :content)")
    db.session.execute(sql, {"title": title, "content": content})
    db.session.commit()


def get_posts():
    sql = text("SELECT id, title, content FROM posts")
    result = db.session.execute(sql)
    return result.fetchall()
