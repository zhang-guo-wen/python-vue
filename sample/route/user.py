from flask import Blueprint
from flask import jsonify

bp = Blueprint("user", __name__, url_prefix="/user")


@bp.route("list")
def user_add():
    return jsonify([1, 2, 3, 7])
