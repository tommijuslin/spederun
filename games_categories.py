from db import db

def add_category(game_id, category_id):
    sql = "INSERT INTO games_categories (game_id, category_id) VALUES (:game_id, :category_id)"
    db.session.execute(sql, {"game_id":game_id, "category_id":category_id})
    db.session.commit()

def get_category_for_game(game_id, category_id):
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
