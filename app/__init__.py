from flask import Flask, render_template, json, jsonify

app = Flask(__name__)
from app.wikipedia import *

@app.route('/')
def render_random_content():
    return render_template('posts.html', articles=get_random_articles(2))


@app.route('/category/<category_name>')
def show_category_posts(category_name):
    return render_template('posts.html', query=category_name, articles=get_articles_for_search(category_name))
