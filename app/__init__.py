from flask import Flask, render_template, json, jsonify

app = Flask(__name__)
from app.wikipedia.content import get_articles as load_content

@app.route('/')
def root():
    return render_template('index.html')

