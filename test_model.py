"""Tests for Melon News App"""
 
from crud import(create_user, get_users, get_user_by_id, get_user_by_user_name, update_user, create_news, get_news_by_id, get_news, update_news, get_comment_by_id, get_comments_by_news_id, create_comment, update_comment, create_category, get_categories, get_category_by_id, update_category)
from unittest import TestCase
from server import app
from model import connect_to_db, db
from flask import session
import server
import unittest
import json
import test_seed
 
class MelonNewsIntergrationTests(unittest.TestCase):
    """Testing for the news feed"""
 
    def setUp(self):
        """Code to run before test"""
 
        self.client = server.app.test_client()
        server.app.config['TESTING'] = True
 
        connect_to_db(server.app, "postgresql:///testmelonnews")
        
        db.create_all()
        test_seed.create_test_data()
 
    def tearDown(self):
        """Code to run after test"""
 
        db.session.remove()
        db.drop_all()
        db.engine.dispose()
 
    def test_homepage():
        """Test to see if hompage works"""
 
        result = self.client.get("/")
        self.assertIn(b"Welcome", result.data)
 
    def test_news_page():
        """Tests to see if news entrys works"""
 
        result = self.client.get("/api/news")
        self.assertIn(b"News", result.data)
 
 
 
if __name__ == "__main__":
    unittest.main()
 
    # User.query.delete()
    # News.query.delete()
    # Comment.query.delete()
 
    # abc = News(title="Type of Melons", summary="Melon Season", article_text="Lorem Ipsum", date_post=datetime(2021, 12, 9))
    # nbc = News(title="Melon Recipe", summary="Melon Salad", article_text="Lorem Ipsum", date_post=datetime(2021, 10, 5))
    # cnn = News(title="Favorite Melons", summary="Favs", article_text="Lorem Ipsum", date_post=datetime(2021, 8, 19))
 
     
    # linda = User(name="Linda", news="abc", comment_text="Love melons")
    # aaron = User(name="Aaron", news="nbc", comment_text="I made it!")
    # chris = User(name="Chris", news="cnn", comment_text="I love watermelon")
 
    # db.session.add_all([abc, nbc, cnn, linda, aaron, chris])
    # db.session.commit()
