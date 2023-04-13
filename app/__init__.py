"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgrq71o2qv2dcb93ifdg-a.oregon-postgres.render.com",
        database="todo_57ep",
        user="root",
        password="v8fgRQ0QSp8WfD0ENyKqA3MIrfFj9Zpw")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
