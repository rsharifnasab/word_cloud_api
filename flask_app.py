
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask import send_file

from src.abr import main as abr_main

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, welcome to this service!'

@app.route('/text2')
def create_from_text():
    print("salam")
    abr_main("google gggggg")
    #return "text"
    return send_file('./out/text.png', mimetype='image/png')
