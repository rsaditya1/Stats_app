from flask import Blueprint, render_template, request, jsonify
import json

views = Blueprint("views", __name__)

# Load stats from file
def load_stats():
    with open("stats.json", "r") as f:
        return json.load(f)

# Save stats to file
def save_stats(stats):
    with open("stats.json", "w") as f:
        json.dump(stats, f, indent=4)

@views.route("/")
def home():
    stats = load_stats()
    return render_template("index.html", stats=stats)

@views.route("/update", methods=["POST"])
def update():
    data = request.get_json()
    stat = data.get("stat")
    stats = load_stats()

    if stat in stats:
        stats[stat] += 1
        save_stats(stats)
        return jsonify({"success": True, "new_value": stats[stat]})
    return jsonify({"success": False}), 400
