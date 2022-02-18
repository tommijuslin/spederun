from db import db

def add_game(title):
    sql = "INSERT INTO games (title) VALUES (:title) RETURNING id"
    id = db.session.execute(sql, {"title":title}).fetchone()[0]
    db.session.commit()

    return id

def get_all_games():
    sql = "SELECT id, title FROM games ORDER BY title"
    return db.session.execute(sql).fetchall()

def get_game(game_id):
    sql = "SELECT id, title FROM games WHERE id=:game_id"
    return db.session.execute(sql, {"game_id":game_id}).fetchone()

def get_game_by_title(title):
    sql = "SELECT id, title FROM games WHERE UPPER(title) LIKE UPPER(:title)"
    return db.session.execute(sql, {"title":title}).fetchone()

def search_games(query):
    sql = "SELECT id, title FROM games WHERE UPPER(title) LIKE UPPER(:query)"
    return db.session.execute(sql, {"query":"%"+query+"%"}).fetchall()

def delete_game(id):
    sql = "DELETE FROM games WHERE id=:id"
    db.session.execute(sql, {"id":id})
    db.session.commit()
