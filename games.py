from db import db

def add_game(title):
    sql = "INSERT INTO games (title) VALUES (:title)"
    db.session.execute(sql, {"title":title})
    db.session.commit()
