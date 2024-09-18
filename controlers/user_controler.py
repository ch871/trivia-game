from flask import Blueprint, jsonify
from dataclasses import asdict
from repositorys.user_repository import find_all_users

user_bluprint = Blueprint("user", __name__)


@user_bluprint.route("/", method=['GET'])
def get_all():
    users = list(map(asdict, find_all_users()))
    return jsonify(users), 200