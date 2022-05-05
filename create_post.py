from data.__all_models import Post
from data import db_session

post = Post()
db_session.global_init("db/food.db")
post.title = input('Введите имя продукта\n').lower()
post.body = input('Введите описание продукта\n')
post.price = int(input('Введите цену продукта\n'))
post.link = input('Введите ссылку на картинку продукта\n')
post.generate_slug()
db_sess = db_session.create_session()
db_sess.add(post)
db_sess.commit()
