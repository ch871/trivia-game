from flask import Flask
from controlers.victory_controler import victory_bluprint
from controlers.question_controler import question_bluprint
from controlers.answer_controler import answer_bluprint
from controlers.user_controler import user_bluprint
from repositorys.create_tables import create_victory_table,drop_all_tables
from service.seed_database import seed_users,seed_trivia


app = Flask(__name__)

if __name__ == '__main__':
    drop_all_tables()
    create_victory_table()
    seed_users()
    seed_trivia()
    app.register_blueprint(user_bluprint, url_prefix="/api/user")
    app.register_blueprint(answer_bluprint, url_prefix="/api/answer")
    app.register_blueprint(question_bluprint, url_prefix="/api/question")
    app.register_blueprint(victory_bluprint, url_prefix="/api/victory")
    app.run(debug=True)

