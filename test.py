from flask import Flask
from data import db_session
from data.jobs import Jobs
from flask import render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/block.db")

    @app.route("/")
    @app.route("/index")
    def index():
        db_sess = db_session.create_session()
        news = db_sess.query(Jobs).filter(Jobs.is_finished != True)
        return render_template("index.html", news=news)

    app.run()


if __name__ == '__main__':
    main()
