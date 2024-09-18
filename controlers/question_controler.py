from flask import Blueprint, jsonify
from dataclasses import asdict
from repositorys.question_reposetory import find_all_questions

question_bluprint = Blueprint("question", __name__)


@question_bluprint.route("/", method=['GET'])
def get_all():
    answer = list(map(asdict, find_all_questions()))
    return jsonify(answer), 200