from unittest import TestCase
from datetime import datetime
from sqlalchemy.sql.sqltypes import DateTime
from server import app
from model import connect_to_db, db, example_data
from flask import session
import crud 

class NewsfeedTestsDatabase(unittest.TestCase):
    """Testing the database"""

def setUp(self):
    """Setting up"""

    self.client = app.test_client()
    app.config['TESTING'] =True

    connect_to_db(app, "postgresql:///testdb")

    db.create_all()
    example_data()

def example_data():
    """Sample data"""

    User.query.delete()
    News.query.delete()
    Comment.query.delete()

    abc = News(title="Type of Melons", summary="Melon Season", article_text="Lorem Ipsum", date_post=datetime(2021, 12, 9))
    nbc = News(title="Melon Recipe", summary="Melon Salad", article_text="Lorem Ipsum", date_post=datetime(2021, 10, 5))
    cnn = News(title="Favorite Melons", summary="Favs", article_text="Lorem Ipsum", date_post=datetime(2021, 8, 19))

     
    linda = User(name="Linda", news="abc", comment_text="Love melons")
    aaron = User(name="Aaron", news="nbc", comment_text="I made it!")
    chris = User(name="Chris", news="cnn", comment_text="I love watermelon")

    db.session.add_all([abc, nbc, cnn, linda, aaron, chris])
    db.session.commit()