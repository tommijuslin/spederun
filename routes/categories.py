from app import app
from flask import render_template, request, redirect, session, url_for
import users
import games
import runs
import categories
import games_categories


@app.route("/game/<int:game_id>/add_category", methods=["get", "post"])
def add_category(game_id):
    if not 'user_id' in session:
        return render_template(
            "error.html", message="You must be logged in to add a category."
        )

    if request.method == "POST":
        category = request.form["category"]

        if len(category) < 1 or len(category) > 20:
            return render_template(
                "add_category.html",
                message="Category name must be 1-20 characters long.",
                game=games.get_game(game_id)
            )

        category_id = categories.get_category(category)

        if not category_id:
            category_id = categories.add_category(category)
        else:
            category_id = category_id[0]
        
        if not games_categories.get_category_for_game(game_id, category_id):
            games_categories.add_category(game_id, category_id)
        
        if "submit_page" in request.form:
            return redirect(url_for("submit_run", id=game_id))

        return redirect(url_for("game", id=game_id))
    
    return render_template("add_category.html", game=games.get_game(game_id))


@app.route("/delete_category/<int:id>", methods=["post"])
def delete_category(id):
    users.check_csrf()
    game_id = request.form["game_id"]
    games_categories.delete_category(game_id, id)
    runs.delete_runs_for_category(game_id, id)

    return redirect(url_for("game", id=game_id))
