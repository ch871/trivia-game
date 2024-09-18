from flask import Blueprint, jsonify
from dataclasses import asdict
from repositorys.answer_repository import find_all_answer

answer_bluprint = Blueprint("answer", __name__)


@answer_bluprint.route("/", method=['GET'])
def get_all():
    answer = list(map(asdict, find_all_answer()))
    return jsonify(answer), 200