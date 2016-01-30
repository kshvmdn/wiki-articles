from flask import Flask, render_template
from app.wikipedia import get_search_articles, get_random_articles

app = Flask(__name__)


@app.route('/')
def show_random_posts():
    return render_template('articles.html', articles=get_random_articles(5))


@app.route('/search/<query>')
@app.route('/category/<query>')
def show_posts(query):
    return render_template('articles.html', query=query,
                           articles=get_search_articles(query))
