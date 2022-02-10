from db import db

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
