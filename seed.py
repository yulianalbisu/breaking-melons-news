import os
from datetime import datetime
import math
import crud
import model
import server
import json

os.system('dropdb testmelonnews')
os.system('createdb testmelonnews')

model.connect_to_db(server.app)
model.db.create_all()

def example_data():

    f = open('seeddata.json',)

    data = json.load(f)

    f.close()
    
    model.Comment.query.delete()
    model.News.query.delete()
    model.User.query.delete()
    model.Category.query.delete()

    users_in_db = []
    categories_in_db = []
    news_in_db = []

    for user in data['users']:
        db_user = crud.create_user(
            user_name=user['user_name'],
            email=user['email'],
            user_role=user['user_role'],
            password=user['password']
        )
        users_in_db.append(db_user)

    for category in data['categories']:
        db_category = crud.create_category(
            category_type=category['category_type'], 
            description=category['description'])
        categories_in_db.append(db_category)

    i=0
    for news in data['news']:
        db_news = crud.create_news(
            user=users_in_db[0],
            category=categories_in_db[i], 
            title=news['title'], 
            summary=news['summary'], 
            article_text=news['article_text'], 
            external_link=news['external_link'], 
            picture_link=news['picture_link'], 
            date_post=datetime(news['date_post'][0], news['date_post'][1], news['date_post'][2])
            )
        i+=1
        news_in_db.append(db_news)

    crud.create_comment(user=users_in_db[1], news=news_in_db[0], comment_text=data['comments'][0]['comment_text'])

example_data()