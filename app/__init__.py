import os
from flask import Flask, render_template
from dotenv import load_dotenv

from .data import EDUCATION, EXPERIENCES, HOBBIES

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template(
        'index.html',
        title="MLH Fellow",
        url=os.getenv("URL"),
        experiences=EXPERIENCES,
        education=EDUCATION,
        hobbies=HOBBIES,
    )
