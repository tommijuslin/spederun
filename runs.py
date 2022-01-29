from db import db

def add_run(game_id, time, platform_id):
    sql = "INSERT INTO runs (time, game_id, platform_id) VALUES (:time, :game_id, :platform_id)"
    db.session.execute(sql, {"time":time, "game_id":game_id, "platform_id":platform_id})
    db.session.commit()

def get_runs_for(game_id):
    sql = """SELECT
                time, platforms.name
             FROM
                runs LEFT JOIN platforms ON runs.platform_id = platforms.id
             WHERE
                game_id=:game_id ORDER BY time"""
    return db.session.execute(sql, {"game_id":game_id}).fetchall()
