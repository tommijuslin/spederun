from app import app
from flask import render_template, request, redirect, session, url_for
from utils import format_time, format_title
import users
import games
import runs


@app.route("/")
def index():
    return render_template(
        "index.html",
        games=games.get_all_games(),
        runs=runs.get_newest_runs(),
        format_time=format_time,
        format_title=format_title,
        admin=users.require_role(1),
    )


@app.route("/result")
def result():
    query = request.args["query"]
    games_list = games.search_games(query)

    if not games_list:
        return render_template("error.html", message="No games found.")

    return render_template("result.html", games=games_list)
