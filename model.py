from sqlalchemy.dialects.postgresql import UUID
from flask_sqlalchemy import SQLAlchemy
import uuid

db = SQLAlchemy()

class User(db.Model):

    __tablename__ = 'users'

    user_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_name = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    user_role = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<User user_name={self.user_name} user_role={self.user_role}>'


class News(db.Model):

    __tablename__ = 'news'

    news_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('users.user_id'), nullable=False)
    category_id = db.Column(UUID(as_uuid=True), db.ForeignKey('categories.category_id'), nullable=False)
    title = db.Column(db.String, nullable=False)
    summary = db.Column(db.Text)
    article_text = db.Column(db.Text)
    external_link = db.Column(db.String)
    picture_link = db.Column(db.String)
    date_post = db.Column(db.DateTime, default=db.func.current_timestamp())

    user = db.relationship('User', backref='users')
    category = db.relationship('Category', backref='categories')

    def __repr__(self):
        return f'<News news_id={self.news_id} title={self.title}>'

    def to_dict(self):
        return {
            'news_id': self.news_id,
            'user_id': self.user_id,
            'user_name': self.user.user_name,
            'category_id': self.category_id,
            'category_type': self.category.category_type,
            'title': self.title,
            'summary': self.summary,
            'article_text': self.article_text,
            'external_link': self.external_link,
            'picture_link': self.picture_link,
            'date_post': self.date_post
        }

class Comment(db.Model):

    __tablename__ = 'comments'

    comment_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('users.user_id'), nullable=False)
    news_id = db.Column(UUID(as_uuid=True), db.ForeignKey('news.news_id'), nullable=False)
    comment_text = db.Column(db.Text)

    commenter_user = db.relationship('User', backref='commenter_users')
    news = db.relationship('News', backref='news')

    def __repr__(self):
        return f'<Comment comment_id={self.comment_id} comment_text={self.comment_text}>'

    def to_dict(self):
        return {
            'comment_id': self.comment_id,
            'user_id': self.user_id,
            'user_name': self.commenter_user.user_name,
            'comment_text': self.comment_text
        }

class Category(db.Model):

    __tablename__ = 'categories'

    category_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    category_type = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Category category_id={self.category_id} category_type={self.category_type}>'

    def to_dict(self):
        return {
            'category_id': self.category_id,
            'category_type': self.category_type,
            'description': self.description
        }
        
def connect_to_db(flask_app, db_uri='postgresql:///testmelonnews', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app

    connect_to_db(app)
