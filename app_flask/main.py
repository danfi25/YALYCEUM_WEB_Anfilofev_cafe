from app_flask.app import app
from app_flask.data import db_session


if __name__ == '__main__':
    db_session.global_init("db/food.db")
    app.run(port=8080, host='127.0.0.1', debug=True)
