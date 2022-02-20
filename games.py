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

def add_platform(game_id, platform_id):
    sql = "INSERT INTO games_platforms (game_id, platform_id) VALUES (:game_id, :platform_id)"
    db.session.execute(sql, {"game_id":game_id, "platform_id":platform_id})
    db.session.commit()

def get_all_platforms(game_id):
    sql = """SELECT platform_id, platforms.name
             FROM games_platforms
             LEFT JOIN platforms
             ON games_platforms.platform_id = platforms.id
             WHERE game_id=:game_id"""
    return db.session.execute(sql, {"game_id":game_id}).fetchall()

def get_platform(game_id, platform_id):
    sql = "SELECT platform_id FROM games_platforms WHERE platform_id=:platform_id AND game_id=:game_id"
    return db.session.execute(sql, {"platform_id":platform_id, "game_id":game_id}).fetchone()

def add_category(game_id, category_id):
    sql = "INSERT INTO games_categories (game_id, category_id) VALUES (:game_id, :category_id)"
    db.session.execute(sql, {"game_id":game_id, "category_id":category_id})
    db.session.commit()

def get_category(game_id, category_id):
    sql = "SELECT game_id, category_id FROM games_categories WHERE game_id=:game_id AND category_id=:category_id"
    return db.session.execute(sql, {"game_id":game_id, "category_id":category_id}).fetchone()

def get_all_categories(game_id):
    sql = """SELECT category_id, categories.category
             FROM games_categories
             LEFT JOIN categories
             ON games_categories.category_id = categories.id
             WHERE game_id=:game_id
             ORDER BY categories.category"""
    return db.session.execute(sql, {"game_id":game_id}).fetchall()

def delete_category(game_id, category_id):
    sql = "DELETE FROM games_categories WHERE game_id=:game_id AND category_id=:category_id"
    db.session.execute(sql, {"game_id":game_id, "category_id":category_id})
    db.session.commit()
