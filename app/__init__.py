import os
from flask import Flask, render_template
from dotenv import load_dotenv

from .data import EDUCATION, EXPERIENCES, HOBBIES, HOBBY_SECTIONS

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


@app.route('/hobbies')
def hobbies():
    return render_template(
        'hobbies.html',
        title="Projects & Interests",
        url=os.getenv("URL"),
        hobby_sections=HOBBY_SECTIONS,
    )
