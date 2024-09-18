from models.answer_model import Answer
from repositorys.create_tables import get_db_connection
from typing import List


def create_answer(answer: Answer) -> int:
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO answers (question_id,incorrect_answer ) VALUES (%s, %s) RETURNING id",
        (answer.question_id, answer.incorrect_answer)
    )
    new_id = cursor.fetchone()['id']
    connection.commit()
    cursor.close()
    connection.close()
    return new_id


def find_all_answer() -> List[Answer]:
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM answers")
    resoult = cursor.fetchall()
    users = [Answer(**answer) for answer in resoult]
    cursor.close()
    connection.close()
    return users


def update_answer(answer: Answer) -> Answer:
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE answers SET question_id = %s, incorrect_answer = %s WHERE id = %s RETURNING * ",
                   (answer.question_id, answer.incorrect_answer)
                   )
    updated_answer = cursor.fetchall()
    return updated_answer


def delete_answer(uid):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE answers WHERE id = %s ", uid)
    return