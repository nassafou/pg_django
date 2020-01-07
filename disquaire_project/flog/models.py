from django.db import models

# Create your models here.
POSTS = [
    {'id': 1, 'title': 'First Post', 'boby': 'this is my first post'},
    {'id': 2, 'title': 'Second Post', 'boby': 'this is my second post'},
    {'id': 3, 'title': 'third Post', 'boby': 'this is my third post'},
]

@classmethod
def all(cls):
    return cls.POSTS

@classmethod
def find(cls, id):
    return cls.POSTS[int(id) -1]