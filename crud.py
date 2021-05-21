from model import db, User, News, Comment, Category, External_News, connect_to_db


### USER ###
def create_user(user_name, user_role, email, password):
    user = User(user_name=user_name, user_role=user_role, email=email, password=password)
    db.session.add(user)
    db.session.commit()
    return User.query.filter(User.user_name == user_name).first()

def get_users():
    return User.query.all()

def get_user_by_id(user_id):
    return User.query.get(user_id)

def get_user_by_user_name(user_name):
    return User.query.filter(User.user_name == user_name).first()

def update_user(user_id, new_data):
    User.query.filter_by(user_id=user_id).update(new_data)
    db.session.commit()
    return User.query.get(user_id)

### NEWS ###
def create_news(user, category, title, summary, article_text, external_link, picture_link, date_post):
    news = News(user=user,
                category=category,
                title=title,
                summary=summary,
                article_text=article_text,
                external_link=external_link,
                picture_link=picture_link,
                date_post=date_post)

    db.session.add(news)
    db.session.commit()
    return news


def get_news_by_id(news_id):
    return News.query.get(news_id)


def get_news():
    return News.query.all()

def update_news(news_id, new_data):
    News.query.filter_by(news_id=news_id).update(new_data)
    db.session.commit()
    return News.query.get(news_id)


### COMMENT ###

def get_comment_by_id(comment_id):
    return Comment.query.get(comment_id)

def get_comments_by_news_id(news_id):
    return News.query.filter(news_id==news_id ).order_by(News.date_post.desc()).all()

def create_comment(user, news, comment_text):
    comment = Comment(commenter_user=user,
                    news=news,
                    comment_text=comment_text)
    db.session.add(comment)
    db.session.commit()
    return comment

def update_comment(comment_id, new_data):
    Comment.query.filter_by(comment_id=comment_id).update(new_data)
    db.session.commit()
    return Comment.query.get(comment_id)

### CATEGORY ###
def create_category(category_type, description):

    category = Category(category_type=category_type, description=description)
    db.session.add(category)
    db.session.commit()
    return category

def get_categories():
    return Category.query.all()

def get_category_by_id(category_id):
    return Category.query.get(category_id)

def update_category(category_id, new_data):
    Category.query.filter_by(category_id=category_id).update(new_data)
    db.session.commit()
    return Category.query.get(category_id)

### EXTERNAL_NEWS ###
def create_external_news(direct_title, direct_link, image):

    external_news = External_News(direct_title=direct_title, direct_link=direct_link, image=image)
    db.session.add(external_news)
    db.session.commit()
    return external_news

def get_external_news():
    return External_News.query.all()

def get_external_news_by_id(external_news_id):
    return External_News.query.get(external_news_id)

def update_external_news(external_news_id, new_data):
    External_News.query.filter_by(external_news_id=external_news_id).update(new_data)
    db.session.commit()
    return External_News.query.get(external_news_id)

if __name__ == '__main__':
    from server import app
    connect_to_db(app)