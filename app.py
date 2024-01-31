from flask import Flask, render_template
import requests
app = Flask(__name__)


@app.route("/")
def index():
    response = requests.get("https://stoic.tekloon.net/stoic-quote")
    data = response.json()
    quote = data["quote"]
    author = data["author"]
    
    return render_template('index.html', quote=quote, author=author)