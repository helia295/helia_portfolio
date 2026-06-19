import os
from flask import Flask, render_template, request, url_for
from dotenv import load_dotenv

from .data import EDUCATION, EXPERIENCES, HOBBIES, HOBBY_SECTIONS

load_dotenv()
app = Flask(__name__)

NAVIGATION = [
    {"endpoint": "index", "label": "Home"},
    {"endpoint": "hobbies", "label": "Projects & Hobbies"},
]


@app.context_processor
def inject_navigation():
    available_endpoints = {rule.endpoint for rule in app.url_map.iter_rules()}
    navigation = [
        {
            "label": item["label"],
            "url": url_for(item["endpoint"]),
            "endpoint": item["endpoint"],
        }
        for item in NAVIGATION
        if item["endpoint"] in available_endpoints
    ]

    return {
        "navigation": navigation,
        "active_endpoint": request.endpoint,
    }


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
