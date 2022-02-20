from app import app
from flask import render_template, request, redirect, session, url_for, jsonify, make_response
from utils import convert_to_ms, validate_time
import users
import games
import runs
import platforms
import categories


NEGATIVE = -1

@app.route("/game/<int:id>/submit_run", methods=["get", "post"])
def submit_run(id):
    if not 'user_id' in session:
        return render_template(
            "error.html", message="You must be logged in to submit a run."
        )

    if request.method == "POST":
        req = request.get_json()
        users.check_csrf(req["csrf_token"])

        time = {
            "hours": validate_time(req["hours"]),
            "minutes": validate_time(req["minutes"]),
            "seconds": validate_time(req["seconds"]),
            "ms": validate_time(req["ms"])
        }

        message = None
        
        if NEGATIVE in time:
            message = "Time must be positive."
        elif all(value == 0 for value in time.values()):
            message = "Time must be non-zero."
        elif not req["selected_category"]:
            message = "No category selected. If no categories exist, create a new category."
        
        if message:
            return make_response(jsonify({"message": message}))

        converted_time = convert_to_ms(time["hours"], time["minutes"], time["seconds"], time["ms"])
        user_id = req["user_id"]
        platform_id = req["selected_platform"]
        category_id = req["selected_category"]
        runs.add_run(id, converted_time, platform_id, user_id, category_id)

        message = None

        if not games.get_platform(id, platform_id):
            games.add_platform(id, platform_id)

        return make_response(jsonify({"redirect": f"/game/{ id }"}))
    
    if not games.get_game(id):
        return render_template("error.html", message=f"No game with id { id } could be found.")
    
    return render_template(
        "submit_run.html",
        game=games.get_game(id),
        platforms=platforms.get_all_platforms(),
        categories=games.get_all_categories(id)
    )


@app.route("/delete_run/<int:id>", methods=["post"])
def delete_run(id):
    users.check_csrf(request.form["csrf_token"])
    runs.delete_run(id)

    if "user_page" in request.form:
        return redirect(url_for("user", id=request.form["user_id"]))
    
    if "game_page" in request.form:
        return redirect(url_for("game", id=request.form["game_id"]))

    return redirect("/")
