from flask import Blueprint, jsonify
from dataclasses import asdict
from repositorys.victories_reposetory import find_all_victory_table

victory_bluprint = Blueprint("victory", __name__)


@victory_bluprint.route("/", method=['GET'])
def get_all():
    victory = list(map(asdict, find_all_victory_table()))
    return jsonify(victory), 200