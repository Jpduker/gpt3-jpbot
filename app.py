from flask import Flask, render_template, request
from datetime import date
import openai
import os
import requests
from dotenv import load_dotenv
from random import choice

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
completion = openai.Completion()

key1 = 'sk-OT1DX8BR9uK1lBJtRJWsT3'
key2 = 'BlbkFJc606VQZz5lOuiIshP06n'
openai.api_key = f"{key1}{key2}"
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')
