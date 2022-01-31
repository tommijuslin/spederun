from db import db

def add_run(game_id, time, platform_id, user_id):
    sql = "INSERT INTO runs (time, game_id, platform_id, user_id) VALUES (:time, :game_id, :platform_id, :user_id)"
    db.session.execute(sql, {"time":time, "game_id":game_id, "platform_id":platform_id, "user_id":user_id})
    db.session.commit()

def get_runs(game_id):
    sql = """SELECT users.username AS user, time, platforms.name AS platform
             FROM runs
             LEFT JOIN platforms
             ON runs.platform_id = platforms.id
             LEFT JOIN users
             ON runs.user_id = users.id
             WHERE
                game_id=:game_id ORDER BY time"""
    return db.session.execute(sql, {"game_id":game_id}).fetchall()
