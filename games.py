from db import db

def add_game(title):
    sql = "INSERT INTO games (title) VALUES (:title)"
    db.session.execute(sql, {"title":title})
    db.session.commit()

def get_all_games():
    sql = "SELECT id, title FROM games ORDER BY title"
    return db.session.execute(sql).fetchall()

def get_game(game_id):
    sql = "SELECT id, title FROM games WHERE id=:game_id"
    return db.session.execute(sql, {"game_id":game_id}).fetchone()
