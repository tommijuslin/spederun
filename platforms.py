from db import db

def add_platform(name):
    sql = """INSERT INTO platforms (name) VALUES (:name)
             ON CONFLICT (name) DO NOTHING
             RETURNING id"""
    id = db.session.execute(sql, {"name":name}).fetchone()[0]
    db.session.commit()
    return id
