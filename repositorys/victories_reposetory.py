from models.victory_table_model import VictoryTable
from repositorys.create_tables import get_db_connection
from typing import List


def create_victory_table(victory: VictoryTable) -> int:
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        """INSERT INTO victories (user_id, question_id, answer, is_correct, time_taken)
         VALUES (%s, %s, %s, %s, %s) RETURNING id""",
        (victory.user_id, victory.question_id, victory.answer_text, victory.is_correct, victory.time_taken)
    )
    new_id = cursor.fetchone()['id']
    connection.commit()
    cursor.close()
    connection.close()
    return new_id


def find_all_victory_table() -> List[VictoryTable]:
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM victories")
    resoult = cursor.fetchall()
    victories = [VictoryTable(**victory) for victory in resoult]
    cursor.close()
    connection.close()
    return victories


def update_victory_table(victory: VictoryTable) -> VictoryTable:
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""UPDATE victories 
    SET user_id = %s, question_id = %s, answer = %s, is_correct = %s, time_taken = %s,
     WHERE id = %s RETURNING * """,
                   (victory.user_id, victory.question_id, victory.answer_text, victory.is_correct, victory.time_taken)
                   )
    updated_question = cursor.fetchall()
    return updated_question


def delete_victory_table(uid):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE victories WHERE id = %s ", uid)
    return
