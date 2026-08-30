# Fixture: Python file with Flask decorators
# Tests both @app.route with methods= and @app.get (Flask 2.0+) and @bp.route
from flask import Blueprint, Flask

app = Flask(__name__)
bp = Blueprint("admin", __name__)


@app.route("/api/admin/stats", methods=["GET"])
def get_stats():
    return {"active_users": 100}


@app.get("/api/admin/settings")
def get_settings():
    return {"theme": "dark"}


@app.post("/api/admin/settings")
def update_settings(data: dict):
    return {"updated": True}


@bp.route("/api/admin/bulk", methods=["PUT"])
def bulk_update():
    return {"processed": 50}


@app.get("/api/items/{item_id}")
def get_item(item_id: str):
    return {"id": item_id}
