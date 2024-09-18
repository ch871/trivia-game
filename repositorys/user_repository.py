from models.user_model import User
from repositorys.create_tables import get_db_connection
from typing import List


def create_user(user: User) -> int:
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO users (first, last, email) VALUES (%s, %s, %s) RETURNING id",
        (user.first, user.last, user.email)
    )
    new_id = cursor.fetchone()['id']
    connection.commit()
    cursor.close()
    connection.close()
    return new_id


def find_all_users() -> List[User]:
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    resoult = cursor.fetchall()
    users = [User(**user) for user in resoult]
    cursor.close()
    connection.close()
    return users


def update_user(user: User) -> User:
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE users SET first = %s, last = %s, email = %s WHERE id = %s RETURNING * ",
                   (user.first, user.last, user.email, user.id)
                   )
    updated_user = cursor.fetchall()
    return updated_user


def delete_user(uid):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE users WHERE id = %s ", uid)
    return
