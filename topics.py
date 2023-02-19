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
    sql = text("INSERT INTO topic (name, content, category_id, created_by) VALUES (:name, :content, :category_id, :created_by)")
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
        "SELECT id, name, content, category_id, created_by FROM topic WHERE category_id=:id")
    result = db.session.execute(sql, {"id": id})
    return result.fetchall()


def get_topic(id):
    sql = text(
        "SELECT id, name, content, category_id, created_by FROM topic WHERE id=:id")
    result = db.session.execute(sql, {"id": id})
    return result.fetchone()


def add_comment(content, topic_id, created_by):
    sql = text(
        "INSERT INTO comment (content, topic_id, created_by) VALUES (:content, :topic_id, :created_by)")
    db.session.execute(
        sql, {"content": content, "topic_id": topic_id, "created_by": created_by})
    db.session.commit()


def get_comments(topic_id):
    sql = text(
        "SELECT id, content, topic_id, created_by FROM comment WHERE topic_id=:topic_id")
    result = db.session.execute(sql, {"topic_id": topic_id})
    return result.fetchall()
