from db import db

def add_category(category):
    sql = "INSERT INTO categories (category) VALUES (:category) RETURNING id"
    id = db.session.execute(sql, {"category":category}).fetchone()[0]
    db.session.commit()
    return id

def get_category(category):
    sql = "SELECT id, category FROM categories WHERE category=:category"
    return db.session.execute(sql, {"category":category}).fetchone()
