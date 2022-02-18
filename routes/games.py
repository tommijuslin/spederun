from app import app
from flask import render_template, request, redirect, session
from utils import format_time
import users
import games
import runs
import platforms
import games_platforms
import categories
import games_categories


@app.route("/game/<int:id>")
def game(id):
    category_id = request.args.get("category")

    if category_id:
        filtered_runs = runs.get_runs_for_category(id, category_id)
    else:
        filtered_runs = runs.get_runs(id)

    game = games.get_game(id)
    if game:
        return render_template(
            "game.html",
            game=game,
            runs=filtered_runs,
            platforms=games_platforms.get_all_platforms(id),
            categories=games_categories.get_all_categories(id),
            format_time=format_time,
            admin=users.require_role(1)
        )
    
    return render_template(
        "error.html", message=f"No game with id { id } could be found."
    )


@app.route("/add_game", methods=["get", "post"])
def add_game():
    if not 'user_id' in session:
        return render_template(
            "error.html", message="You must be logged in to add a game."
        )

    if request.method == "POST":
        title = request.form["title"]
        if len(title) > 50 or len(title) < 1:
            return render_template(
                "add_game.html", message="Game title must be 1-50 characters long."
            )
        if games.get_game_by_title(title):
            return render_template("add_game.html", message="Game already exists.")

        games.add_game(title)

        return redirect("/")
    
    return render_template("add_game.html")


@app.route("/delete_game/<int:id>", methods=["post"])
def delete_game(id):
    users.check_csrf()
    games.delete_game(id)

    return redirect("/")
