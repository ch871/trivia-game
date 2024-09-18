import psycopg2
from psycopg2.extras import RealDictCursor
from config.sql_config import SQLALCHEMY_DATABASE_URI


def get_db_connection():
    return psycopg2.connect(SQLALCHEMY_DATABASE_URI, cursor_factory=RealDictCursor)


def create_user_table():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        first VARCHAR(100) NOT NULL,
        last VARCHAR(100) NOT NULL,
        email VARCHAR(100) NOT NULL
    )
    ''')
    connection.commit()
    cursor.close()
    connection.close()


def create_question_table():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS questions (
        id SERIAL PRIMARY KEY,
        question VARCHAR(300) NOT NULL,
        current_answer VARCHAR(225) NOT NULL
    )
    ''')
    connection.commit()
    cursor.close()
    connection.close()


def create_answer_table():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS answers (
        id SERIAL PRIMARY KEY,
        question_id INTEGER NOT NULL,
        incorrect_answer VARCHAR(255) NOT NULL,
        FOREIGN KEY (question_id) REFERENCES questions(id) ON DELETE CASCADE
    )
    ''')
    connection.commit()
    cursor.close()
    connection.close()


def create_victory_table():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS victories (
        id SERIAL PRIMARY KEY,
        user_id INTEGER NOT NULL,
        question_id INTEGER NOT NULL,
        answer VARCHAR(255) NOT NULL,
        is_correct boolean,
        time_taken interval,
        FOREIGN KEY (question_id) REFERENCES questions(id) ON DELETE CASCADE,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
    )
    ''')
    connection.commit()
    cursor.close()
    connection.close()