"""Tests for Melon News App"""
import os
import crud
from unittest import TestCase
from server import app
from model import connect_to_db, db, User, Comment, News, Category, External_News
from flask import session
import unittest
import json
from seed import example_data
from datetime import datetime

class MelonTestsDatabase(TestCase):
    def setUp(self):
        """Run code before every test"""

        # Get the Flask test client
        app.config['TESTING'] = True
        self.client = app.test_client()

        # Connect to test database
        os.system('dropdb testdbmelonnews')
        os.system('createdb testdbmelonnews')

        connect_to_db(app, "postgresql:///testdbmelonnews")
        db.create_all()

        Comment.query.delete()
        News.query.delete()
        User.query.delete()
        Category.query.delete()
        External_News.query.delete()

        example_data()
        
    def tearDown(self):
        """Run this at the end of every test."""

        db.session.remove()
        db.drop_all()
        db.engine.dispose()

    def test_user_create(self):
        user = crud.create_user(user_name = "Bob Melon", user_role= "admin", email ="bob@bobmelon.net", password = "123456")
        print(user)
        self.assertIsInstance(user, User)

    def test_email(self):
        user = crud.create_user(user_name = "Bob Melon", user_role= "admin", email ="bob@bobmelon.net", password = "123456")
        self.assertEqual('bob@bobmelon.net', user.email)
        print(user.email)

    def test_email_not_in_user(self):
        user = crud.create_user(user_name = "Bob Melon", user_role= "admin", email ="bob@bobmelon.net", password = "123456")
        self.assertNotEqual('lime0@citrus.com', user.email)
        print(user.email)

    def test_news_create(self):
        user = crud.create_user(user_name = "Bob Melon", user_role= "admin", email ="bob@bobmelon.net", password = "123456")
        category = crud.create_category(category_type="breaking news", description="cutting edge stories")
        news = crud.create_news(
            user=user, 
            category=category, 
            title="Shocking New Revelations", 
            summary="Our corresponding tells the shocking tale.",
            article_text="Melon info that's very important.",
            external_link="https://fellowship.hackbrightacademy.com/",
            picture_link="https://media.npr.org/assets/img/2011/07/26/melonmain_wide-ea71c1090ecb973e0098d2889a1560cb42f73dad-s800-c85.jpg",
            date_post=datetime(2021, 6, 1)
            )
        self.assertIsInstance(news, News)
        print(news)

    def test_news_category(self):
        user = crud.create_user(user_name = "Bob Melon", user_role= "admin", email ="bob@bobmelon.net", password = "123456")
        category = crud.create_category(category_type="breaking news", description="cutting edge stories")
        news = crud.create_news(
            user=user, 
            category=category, 
            title="Shocking New Revelations", 
            summary="Our corresponding tells the shocking tale.",
            article_text="Melon info that's very important.",
            external_link="https://fellowship.hackbrightacademy.com/",
            picture_link="https://media.npr.org/assets/img/2011/07/26/melonmain_wide-ea71c1090ecb973e0098d2889a1560cb42f73dad-s800-c85.jpg",
            date_post=datetime(2021, 6, 1)
            )
        self.assertEqual(category.category_id, news.category_id)

    def test_news_user(self):
        user = crud.create_user(user_name = "Bob Melon", user_role= "admin", email ="bob@bobmelon.net", password = "123456")
        category = crud.create_category(category_type="breaking news", description="cutting edge stories")
        news = crud.create_news(
            user=user, 
            category=category, 
            title="Shocking New Revelations", 
            summary="Our corresponding tells the shocking tale.",
            article_text="Melon info that's very important.",
            external_link="https://fellowship.hackbrightacademy.com/",
            picture_link="https://media.npr.org/assets/img/2011/07/26/melonmain_wide-ea71c1090ecb973e0098d2889a1560cb42f73dad-s800-c85.jpg",
            date_post=datetime(2021, 6, 1)
            )
        self.assertEqual(user.user_id, news.user_id)
 
if __name__ == "__main__":
    unittest.main()