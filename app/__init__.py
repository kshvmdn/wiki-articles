from flask import Flask, render_template, json, jsonify

app = Flask(__name__)
from app.wikipedia import get_articles as load_content

@app.route('/')
def render_random_content():
    content = load_content()
    return render_template('posts.html', articles=content)


