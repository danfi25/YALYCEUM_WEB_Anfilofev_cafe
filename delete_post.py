from data.__all_models import Post
from data import db_session

user = Post()
db_session.global_init("db/food.db")
db_sess = db_session.create_session()
post = db_sess.query(Post).filter(Post.title == input('Введите имя блюда\n').lower()).first()
db_sess.delete(post)
db_sess.commit()
