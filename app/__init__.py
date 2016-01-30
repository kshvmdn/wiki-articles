from flask import Flask, render_template, json, jsonify
from app.wikipedia import get_search_articles, get_random_articles

app = Flask(__name__)


@app.route('/')
def render_random_content():
    return render_template('posts.html', articles=get_random_articles(5))


@app.route('/search/<query>')
@app.route('/category/<query>')
def show_posts(query):
    return render_template('posts.html', query=query, articles=get_search_articles(query))
