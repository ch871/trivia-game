from repositorys.create_tables import create_user_table, create_answer_table, create_question_table
from api.requets import get_users, get_trivia
from models.user_model import User
from models.quwestion_model import Question
from models.answer_model import Answer
from toolz import get_in
from repositorys.user_repository import create_user
from repositorys.question_reposetory import create_questions
from repositorys.answer_repository import create_answer



def seed_users():
    create_user_table()
    users = get_users()
    for user_from_api in users['results']:
        user = User(first=get_in(['name', 'first'], user_from_api),
                    last=get_in(['name', 'last'], user_from_api),
                    email=user_from_api['email']
                    )
        create_user(user)
# seed_users()


def seed_trivia():
    create_question_table()
    create_answer_table()
    questions = get_trivia()

    for question_from_api in questions['results']:
        question = Question(question_text=question_from_api['question'],
                        correct_answer=question_from_api['correct_answer']
                        )
        quest_id = create_questions(question)
        for incorrect_answer in question_from_api['incorrect_answers']:
            answer = Answer(incorrect_answer=incorrect_answer,
                            question_id=quest_id)
            create_answer(answer)

# seed_trivia()

