"""Script to seed a test database"""

import os
import json
from random import choice, randint
from datetime import DateTime
import crud
import model
import server

os.system('dropdb melon_news')
os.system('createdb melon_news')

model.connect_to_db(server.app)
model.db.create_all()

def test_example_data():

    with open('test_melon_news.json') as f:
        melon_news_data = json.loads(f.read())
    
    melon_news_in_db = []
    for melon_news in melon_news_data:
        comment = melon_news['comment']
        news = melon_news['news']
        user = melon_news['user']
        category = melon_news['category']

        db_melon_news = crud.create_melon_news(comment, news, user, category)
    
    model.Comment.query.delete()
    model.News.query.delete()
    model.User.query.delete()
    model.Category.query.delete()

    users_in_db = {}
    categories_in_db = {}
    news_in_db = {}

    for user in melon_news_data['users']:
        db_user = crud.create_user(
            user_name=user['user_name'],
            email=user['email'],
            user_role=user['user_role'],
            password=user['password']
        )
        users_in_db[db_user.email] = db_user

    for category in melon_news_data['categories']:
        db_category = crud.create_category(
            category_type=category['category_type'], 
            description=category['description'])
        categories_in_db[db_category.category_type] = db_category

    for news in melon_news_data['news']:
        db_news = crud.create_news(
            user=users_in_db[news['email']],
            category=categories_in_db[news['category_type']], 
            title=news['title'], 
            summary=news['summary'], 
            article_text=news['article_text'], 
            external_link=news['external_link'], 
            picture_link=news['picture_link'], 
            date_post=DateTime(news['date_post'][0], news['date_post'][1], news['date_post'][2])
            )
        news_in_db[db_news.title] = db_news

    for comment in melon_news_data['comments']:
        crud.create_comment(
            user=users_in_db[comment['email']], 
            news=news_in_db[comment['title']], 
            comment_text=comment['comment_text']
            )

    return melon_news_in_db