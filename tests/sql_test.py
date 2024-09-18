import pytest
from repositorys.create_tables import create_victory_table,drop_all_tables
from service.seed_database import seed_users,seed_trivia
from repositorys.user_repository import find_all_users,create_user
from repositorys.answer_repository import find_all_answer,create_answer
from repositorys.question_reposetory import find_all_questions,create_questions
from repositorys.victories_reposetory import find_all_victory_table,create_victory_table as c_victory
from models.user_model import User
from models.answer_model import Answer
from models.victory_table_model import VictoryTable
from models.quwestion_model import Question
from toolz import first

@pytest.fixture(scope="module")
def setup_database():
    create_victory_table()
    seed_users()
    seed_trivia()
    yield
    drop_all_tables()


def test_find_all_users():
    users = find_all_users()
    assert len(users) >= 0


def test_create_user():
    user_id = create_user(User(
        email='fdsa',last='shtern',first='mordechaim'
        )
    )
    assert user_id


def test_find_all_answer():
    answers = find_all_answer()
    assert len(answers) >= 0


def test_create_answer():
    answer = create_answer(Answer(
        incorrect_answer='treds', question_id=(first(find_all_questions())).id
        )
    )
    assert answer


def test_find_all_questions():
    questions = find_all_questions()
    assert len(questions) >= 0


def test_create_questions():
    question = create_questions(Question(
        question_text='whay tomer dictionery',correct_answer="stam"
        )
    )
    assert question


def test_find_all_victory_table():
    victories = find_all_victory_table()
    assert len(victories) >= 0


def test_create_victory():
    victpry_id = c_victory(VictoryTable(
        question_id=(first(find_all_questions())).id,
        user_id=(first(test_find_all_users())).id,
        is_correct=True,
        answer_text='ertt'
        )
    )
    assert victpry_id