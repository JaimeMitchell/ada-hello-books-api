
from app import db


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    books = db.relationship("Book", back_populates="author")

    def to_dict(self):  # GET/READ
        author_as_dict = {}
        author_as_dict["id"] = self.id
        author_as_dict["name"] = self.name

        return author_as_dict

    @classmethod
    def from_dict(cls, author_data):  # POST/CREATE
        new_author = Author(name=author_data["name"])
        return new_author