from flask import Flask

from flask import render_template
from data.__all_models import Post
from data import db_session

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/team')
def team():
    return render_template('team.html')


@app.route('/shopping-cart')
def shopping_cart():
    return render_template('shopping-cart.html')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


@app.route('/products')
def products():
    db_sess = db_session.create_session()
    posts = db_sess.query(Post).all()
    return render_template('products.html', posts=posts)


@app.route('/<slug>')
def post_detail(slug):
    db_sess = db_session.create_session()
    post = db_sess.query(Post).filter(Post.slug == slug).first()
    return render_template('product.html', posts=post)


if __name__ == '__main__':
    db_session.global_init("db/food.db")
    app.run(port=8080, host='127.0.0.1', debug=True)