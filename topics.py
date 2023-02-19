import os
from flask import request, session, abort
from db import db
import secrets
from sqlalchemy.sql import text


def add_category(name):
    sql = text("INSERT INTO category (name) VALUES (:name)")
    db.session.execute(sql, {"name": name})
    db.session.commit()


def add_topic(name, content, category_id, created_by):
    sql = text("INSERT INTO topics (name, content, category_id, created_by) VALUES (:name, :content, :category_id, :created_by)")
    db.session.execute(sql, {"name": name, "content": content,
                       "category_id": category_id, "created_by": created_by, })
    db.session.commit()


def get_categories():
    sql = text("SELECT id, name FROM category")
    result = db.session.execute(sql)
    return result.fetchall()


def get_category(id):
    sql = text("SELECT id, name FROM category WHERE id=:id")
    result = db.session.execute(sql, {"id": id})
    return result.fetchone()


def get_topics(id):
    sql = text(
        "SELECT id, name, content, category_id, created_by, timestamp FROM topics WHERE category_id=:id")
    result = db.session.execute(sql, {"id": id})
    return result.fetchall()
