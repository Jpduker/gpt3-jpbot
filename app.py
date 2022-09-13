from flask import Flask, render_template, request, jsonify
from datetime import date
import openai
import os
import requests
from dotenv import load_dotenv
from random import choice
import jpBot

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
completion = openai.Completion()

key1 = 'sk-ZUnZBCrWVFwGTho6IU8cT3'
key2 = 'BlbkFJfbbBztu3Y7Gi2Dc1lGfV'
openai.api_key = f"{key1}{key2}"

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route('/model', methods=['GET', 'POST'])
def model():
    result = "Not Found"
    if request.method == 'POST':
        result = jpBot.ask(request.get_json())
        return jsonify(result)
