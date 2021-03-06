from flask import (Flask, jsonify, render_template, request, session)
from jinja2 import StrictUndefined
from model import connect_to_db
import crud
from datetime import datetime
import json

app = Flask(__name__)

app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def index():
    """View index."""
    return render_template('index.html')

###  ENDPOINTS ####

### NEWS ###

@app.route('/api/news')
def get_news():
    """Gets list of news entries."""
    news_data = crud.get_news()
    news_list = []
    for news in news_data:
        news_list.append(news.to_dict())
    return jsonify(news_list)

### EXTERNAL NEWS ###

@app.route('/api/external-news')
def get_external_news():
    """Gets list of external news entries."""
    external_news_data = crud.get_external_news()
    external_news_list = []
    for news in external_news_data:
        external_news_list.append(news.to_dict())
    return jsonify(external_news_list)


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
    session.clear()
