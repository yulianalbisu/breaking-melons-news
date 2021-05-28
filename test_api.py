from unittest import TestCase
from server import app
from flask import json
from model import connect_to_db, db, User, Comment, News, Category, External_News
import os
from seed import example_data

class TestMelonNews(TestCase):
    """Flask tests."""

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

    def test_get_news_list(self):
        result = self.client.get("/api/news")
        data = result.get_json()
        self.assertEqual("Mel Melitpolski", data[0]['user_name'])

    def test_get_external_news_list(self):
        result = self.client.get("/api/external-news")
        data = result.get_json()
        self.assertIn("The Mysterious Melonicorn", data[0]['direct_title'])

if __name__ == "__main__":
    import unittest

    unittest.main()
