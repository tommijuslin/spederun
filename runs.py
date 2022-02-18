from db import db

def add_run(game_id, time, platform_id, user_id, category_id):
    sql = """INSERT INTO runs (time, game_id, platform_id, user_id, date, category_id)
             VALUES (:time, :game_id, :platform_id, :user_id, NOW(), :category_id)"""
    db.session.execute(sql, {"time":time, "game_id":game_id, "platform_id":platform_id, "user_id":user_id, "category_id":category_id})
    db.session.commit()

def get_runs(game_id):
    sql = """SELECT
             runs.id,
             users.username AS user,
             user_id,
             time,
             categories.category AS category,
             platforms.name AS platform,
             date::timestamp::date
             FROM runs
             LEFT JOIN platforms
             ON runs.platform_id = platforms.id
             LEFT JOIN users
             ON runs.user_id = users.id
             LEFT JOIN categories
             ON runs.category_id = categories.id
             WHERE game_id=:game_id ORDER BY time"""
    return db.session.execute(sql, {"game_id":game_id}).fetchall()

def get_newest_runs():
    sql = """SELECT
             runs.id,
             users.username AS user,
             user_id,
             time,
             platforms.name AS platform,
             games.title AS game,
             game_id,
             date::timestamp::date
             FROM runs
             LEFT JOIN platforms
             ON runs.platform_id = platforms.id
             LEFT JOIN users
             ON runs.user_id = users.id
             LEFT JOIN games
             ON runs.game_id = games.id
             ORDER BY runs.date DESC LIMIT 5"""
    return db.session.execute(sql).fetchall()

def get_runs_for_user(user_id):
    sql = """SELECT
             runs.id,
             users.username AS user,
             user_id,
             time,
             platforms.name AS platform,
             games.title AS game,
             game_id,
             date::timestamp::date
             FROM runs
             LEFT JOIN platforms
             ON runs.platform_id = platforms.id
             LEFT JOIN users
             ON runs.user_id = users.id
             LEFT JOIN games
             ON runs.game_id = games.id
             WHERE user_id=:user_id ORDER BY game"""
    return db.session.execute(sql, {"user_id":user_id}).fetchall()

def get_runs_for_category(game_id, category_id):
    sql = """SELECT
             runs.id,
             users.username AS user,
             user_id,
             time,
             platforms.name AS platform,
             games.title AS game,
             game_id,
             category_id,
             categories.category AS category,
             date::timestamp::date
             FROM runs
             LEFT JOIN platforms
             ON runs.platform_id = platforms.id
             LEFT JOIN users
             ON runs.user_id = users.id
             LEFT JOIN games
             ON runs.game_id = games.id
             LEFT JOIN categories
             ON runs.category_id = categories.id
             WHERE game_id=:game_id AND category_id=:category_id ORDER BY time"""
    return db.session.execute(sql, {"game_id":game_id, "category_id":category_id}).fetchall()

def delete_run(id):
    sql = "DELETE FROM runs WHERE id=:id"
    db.session.execute(sql, {"id":id})
    db.session.commit()

def delete_runs_for_category(game_id, category_id):
    sql = "DELETE FROM runs WHERE game_id=:game_id AND category_id=:category_id"
    db.session.execute(sql, {"game_id":game_id, "category_id":category_id})
    db.session.commit()
