import json
from flaskapp import db, app
from sqlalchemy.dialects.postgresql import JSON


class Document_DBModel(db.Model):
    __tablename__ = 'documents'
    id = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.Text, db.ForeignKey('users.id', ondelete='CASCADE'))
    document_type = db.Column(db.Text, nullable=False)
    location = db.Column(db.Text, nullable=False)

    def __init__(self, owner, document_type, location):
        self.owner = owner
        self.document_type = document_type
        self.location = location

