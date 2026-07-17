# tests.py
import unittest
from peewee import *
from app import TimelinePost
from playhouse.shortcuts import model_to_dict

MODELS = [TimelinePost]

# use an in-memory SQLite for tests.
test_db = SqliteDatabase(':memory:')

class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        # Bind model classes to test db. Since we have a complete list of
        # all models, we do not need to recursively bind dependencies.
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)

        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        # Not strictly necessary since SQLite in-memory databases only live
        # for the duration of the connection, and in the next step we close
        # the connection...but a good practice all the same.
        test_db.drop_tables(MODELS)

        # Close connection to db.
        test_db.close()

        # If we wanted, we could re-bind the models to their original
        # database here. But for tests this is probably not necessary.
    
    def test_timeline_post(self):
        first_post = TimelinePost.create(name="John Doe",email="john@example.com",content='Hello world, I\'m John!')
        assert first_post.id == 1
        second_post = TimelinePost.create(name="Jane Doe",email="jane@example.com",content='Hello world, I\'m Jane!')
        assert second_post.id == 2
        
        get_timeline_posts =  {
                'timeline_posts': [
                model_to_dict(post)
                for post in TimelinePost.select().order_by(TimelinePost.created_at.desc())
            ]
        }
        
        for post in get_timeline_posts['timeline_posts']:
            if(post['id'] == 1):
                assert post['name'] == first_post.name
                assert post['email'] == first_post.email
                assert post['content'] == first_post.content
            if(post['id'] == 2):
                assert post['name'] == second_post.name
                assert post['email'] == second_post.email
                assert post['content'] == second_post.content
        