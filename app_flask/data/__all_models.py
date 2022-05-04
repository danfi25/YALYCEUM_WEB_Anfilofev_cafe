from app_flask.data.db_session import SqlAlchemyBase
import sqlalchemy
from datetime import datetime
import re


def slugify(s):
    pattern = r'\[^\w+]'
    return re.sub(pattern, '-', s)


class Post(SqlAlchemyBase):
    __tablename__ = 'food'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    title = sqlalchemy.Column(sqlalchemy.String(140))
    slug = sqlalchemy.Column(sqlalchemy.String(140), unique=True)
    body = sqlalchemy.Column(sqlalchemy.Text)
    created = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now())
    link = sqlalchemy.Column(sqlalchemy.Text, unique=True)
    price = sqlalchemy.Column(sqlalchemy.Float)

    def __init__(self):
        self.generate_slug()

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return f'<Post id: {self.id}, title: {self.title}>'


