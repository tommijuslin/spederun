from db import db

def add_category(category):
    sql = "INSERT INTO categories (category) VALUES (:category) RETURNING id"
    id = db.session.execute(sql, {"category":category}).fetchone()[0]
    db.session.commit()
    return id

def get_category(category):
    sql = "SELECT id, category FROM categories WHERE category=:category"
    return db.session.execute(sql, {"category":category}).fetchone()

def delete_category(id):
    sql = "DELETE FROM categories WHERE id=:id"
    db.session.execute(sql, {"id":id})
    db.session.commit()
