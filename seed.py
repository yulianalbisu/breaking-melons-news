import os
from datetime import datetime
import math
import crud
import model
import server
import json



def example_data():

    os.system('dropdb testmelonnews')
    os.system('createdb testmelonnews')

    model.connect_to_db(server.app)
    model.db.create_all()

    f = open('seeddata.json',)

    data = json.load(f)

    f.close()
    
    f2 = open('direct-link.json',)

    direct_link_data = json.load(f2)

    f2.close()

    model.Comment.query.delete()
    model.News.query.delete()
    model.User.query.delete()
    model.Category.query.delete()
    model.External_News.query.delete()

    users_in_db = {}
    categories_in_db = {}
    news_in_db = {}

    for user in data['users']:
        db_user = crud.create_user(
            user_name=user['user_name'],
            email=user['email'],
            user_role=user['user_role'],
            password=user['password']
        )
        users_in_db[db_user.email] = db_user

    for category in data['categories']:
        db_category = crud.create_category(
            category_type=category['category_type'], 
            description=category['description'])
        categories_in_db[db_category.category_type] = db_category

    for news in data['news']:
        db_news = crud.create_news(
            user=users_in_db[news['email']],
            category=categories_in_db[news['category_type']], 
            title=news['title'], 
            summary=news['summary'], 
            article_text=news['article_text'], 
            external_link=news['external_link'], 
            picture_link=news['picture_link'], 
            date_post=datetime(news['date_post'][0], news['date_post'][1], news['date_post'][2])
            )
        news_in_db[db_news.title] = db_news

    for comment in data['comments']:
        crud.create_comment(
            user=users_in_db[comment['email']], 
            news=news_in_db[comment['title']], 
            comment_text=comment['comment_text']
            )

    for direct_link_item in direct_link_data:
        crud.create_external_news(
            direct_title=direct_link_item['direct_title'],
            direct_link=direct_link_item['direct_link'],
            image=direct_link_item['image']
        )


example_data()