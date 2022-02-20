from app import app
from flask import render_template, request, redirect, session, url_for, jsonify, make_response
import users
import games
import runs
import categories


@app.route("/game/<int:game_id>/add_category", methods=["get", "post"])
def add_category(game_id):
    if not 'user_id' in session:
        return render_template(
            "error.html", message="You must be logged in to add a category."
        )

    if request.method == "POST":
        req = request.get_json()
        category = req["category"]

        if len(category) < 1 or len(category) > 20:
            return make_response(jsonify({"message": "Category name must be 1-20 characters long."}))

        category_id = categories.get_category(category)

        if not category_id:
            category_id = categories.add_category(category)
        else:
            category_id = category_id[0]
        
        new_category = False
        message = None

        if not games.get_category(game_id, category_id):
            games.add_category(game_id, category_id)
            new_category = True
            message = "Category added."

        return make_response(jsonify({
            "redirect": f'/game/{ game_id }',
            "category_id": category_id,
            "category": category,
            "new": new_category,
            "message": message,
        }))
    
    return render_template("add_category.html", game=games.get_game(game_id))


@app.route("/delete_category/<int:id>", methods=["post"])
def delete_category(id):
    users.check_csrf(request.form["csrf_token"])
    game_id = request.form["game_id"]
    games.delete_category(game_id, id)
    runs.delete_runs_for_category(game_id, id)

    return redirect(url_for("game", id=game_id))
