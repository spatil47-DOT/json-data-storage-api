"""
Author- Suraj Prakash Patil
Date- 11/06/2024

"""

from . import db
from sqlalchemy.dialects.postgresql import JSON

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(JSON)
