import datetime
import os
import re
import time
from flask import Flask, render_template, request, url_for
from dotenv import load_dotenv
from peewee import CharField, DateTimeField, Model, MySQLDatabase, SqliteDatabase, TextField
from playhouse.shortcuts import model_to_dict

from .data import EDUCATION, EXPERIENCES, HOBBIES, HOBBY_SECTIONS, VISITED_PLACES

load_dotenv()
app = Flask(__name__)

EMAIL_REGEX = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
CONTROL_CHAR_REGEX = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]")
MAX_NAME_LENGTH = 80
MAX_EMAIL_LENGTH = 254
MAX_CONTENT_LENGTH = 500

if os.getenv("TESTING") == "true":
    print("Running in test mode")
    mydb = SqliteDatabase('file:memory?mode=memory&cache=shared', uri=True)
else:
    mydb = MySQLDatabase(
        os.getenv("MYSQL_DATABASE"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        host=os.getenv("MYSQL_HOST"),
        port=3306,
    )

print(mydb)


class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb


for attempt in range(30):
    try:
        mydb.connect(reuse_if_open=True)
        mydb.create_tables([TimelinePost])
        break
    except Exception:
        if attempt == 29:
            raise
        time.sleep(2)

NAVIGATION = [
    {"endpoint": "index", "label": "Home"},
    {"endpoint": "hobbies", "label": "Projects & Hobbies"},
    {"endpoint": "map_page", "label": "Map"},
    {"endpoint": "timeline", "label": "Timeline"},
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


@app.route("/")
def index():
    return render_template(
        "index.html",
        title="Helia Dinh",
        url=os.getenv("URL"),
        experiences=EXPERIENCES,
        education=EDUCATION,
        hobbies=HOBBIES,
    )


@app.route("/hobbies")
def hobbies():
    return render_template(
        "hobbies.html",
        title="Projects & Interests",
        url=os.getenv("URL"),
        hobby_sections=HOBBY_SECTIONS,
        visited_places=VISITED_PLACES,
    )


@app.route("/map")
def map_page():
    return render_template(
        "map.html",
        title="Places I've Visited",
        url=os.getenv("URL"),
        visited_places=VISITED_PLACES,
    )


@app.route("/timeline")
def timeline():
    return render_template(
        "timeline.html",
        title="Timeline",
        url=os.getenv("URL"),
    )


@app.route("/health")
def health():
    try:
        mydb.connect(reuse_if_open=True)
        mydb.execute_sql("SELECT 1").fetchone()
    except Exception as error:
        return {
            "status": "error",
            "database": "error",
            "message": str(error),
        }, 503

    return {
        "status": "ok",
        "database": "ok",
    }


def validation_error(message, field):
    return {
        "error": message,
        "field": field,
    }, 400


def clean_form_value(field):
    return (request.form.get(field) or "").strip()


def validate_timeline_post(name, email, content):
    if not name:
        return validation_error("Please enter your name.", "name")
    if len(name) > MAX_NAME_LENGTH:
        return validation_error("Name must be 80 characters or fewer.", "name")
    if CONTROL_CHAR_REGEX.search(name):
        return validation_error("Name contains unsupported characters.", "name")

    if not email:
        return validation_error("Please enter your email address.", "email")
    if len(email) > MAX_EMAIL_LENGTH:
        return validation_error("Email must be 254 characters or fewer.", "email")
    if CONTROL_CHAR_REGEX.search(email) or not EMAIL_REGEX.match(email):
        return validation_error("Please enter a valid email address.", "email")

    if not content:
        return validation_error("Please enter a timeline post.", "content")
    if len(content) > MAX_CONTENT_LENGTH:
        return validation_error("Post must be 500 characters or fewer.", "content")
    if CONTROL_CHAR_REGEX.search(content):
        return validation_error("Post contains unsupported characters.", "content")

    return None


@app.route("/api/timeline_post", methods=["POST"])
def post_timeline_post():
    name = clean_form_value("name")
    email = clean_form_value("email").lower()
    content = clean_form_value("content")

    error = validate_timeline_post(name, email, content)
    if error:
        return error

    timeline_post = TimelinePost.create(name=name, email=email, content=content)

    return model_to_dict(timeline_post)


@app.route("/api/timeline_post", methods=["GET"])
def get_timeline_post():
    return {
        "timeline_posts": [
            model_to_dict(post)
            for post in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }


@app.route("/api/timeline_post/<int:post_id>", methods=["DELETE"])
def delete_timeline_post(post_id):
    timeline_post = TimelinePost.get_or_none(TimelinePost.id == post_id)

    if timeline_post is None:
        return {"error": "Timeline post not found"}, 404

    deleted_post = model_to_dict(timeline_post)
    timeline_post.delete_instance()

    return deleted_post
