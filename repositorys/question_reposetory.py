from models.quwestion_model import Question
from repositorys.create_tables import get_db_connection
from typing import List


def create_questions(question: Question) -> int:
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO questions (question, current_answer ) VALUES (%s, %s) RETURNING id",
        (question.question_text, question.correct_answer)
    )
    new_id = cursor.fetchone()['id']
    connection.commit()
    cursor.close()
    connection.close()
    return new_id


def find_all_questions() -> List[Question]:
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM question")
    resoult = cursor.fetchall()
    users = [Question(**question) for question in resoult]
    cursor.close()
    connection.close()
    return users


def update_questions(question: Question) -> Question:
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE questions SET question = %s, current_answer = %s WHERE id = %s RETURNING * ",
                   (question.question_text, question.correct_answer, question.id)
                   )
    updated_question = cursor.fetchall()
    return updated_question


def delete_questions(uid):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE questions WHERE id = %s ", uid)
    return