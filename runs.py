from db import db

def add_run(game_id, time):
    sql = "INSERT INTO runs (time, game_id) VALUES (:time, :game_id)"
    db.session.execute(sql, {"time":time, "game_id":game_id})
    db.session.commit()

def get_runs_for(game_id):
    sql = "SELECT * FROM runs WHERE game_id=:game_id"
    return db.session.execute(sql, {"game_id":game_id}).fetchall()
