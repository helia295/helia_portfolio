import datetime
import os
import re
from flask import Flask, render_template, request, url_for
from dotenv import load_dotenv
from peewee import CharField, DateTimeField, Model, MySQLDatabase, SqliteDatabase, TextField
from playhouse.shortcuts import model_to_dict

from .data import EDUCATION, EXPERIENCES, HOBBIES, HOBBY_SECTIONS, VISITED_PLACES

load_dotenv()
app = Flask(__name__)

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


mydb.connect(reuse_if_open=True)
mydb.create_tables([TimelinePost])

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


@app.route("/api/timeline_post", methods=["POST"])
def post_timeline_post():
    EMAIL_REGEX = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
    name = request.form.get("name")
    email = request.form.get("email")
    content = request.form.get("content")

    if not name:
        return "Invalid name", 400
    if not email or not EMAIL_REGEX.match(email):
        return "Invalid email", 400
    if not content:
        return "Invalid content", 400

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
