from db import db

def add_platform_to_game(game_id, platform_id):
    sql = "INSERT INTO games_platforms (game_id, platform_id) VALUES (:game_id, :platform_id)"
    db.session.execute(sql, {"game_id":game_id, "platform_id":platform_id})
    db.session.commit()

def get_platforms_for_game(game_id):
    sql = "SELECT platform_id FROM games_platforms WHERE game_id=:game_id"
    return db.session.execute(sql, {"game_id":game_id}).fetchall()
