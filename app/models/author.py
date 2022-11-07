from app import db


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    books = db.relationship("Book", back_populates="author")
    # THE ONE, PARENT, only has db.relationship, NO db.foreignkey

    def to_dict(self):
        author_as_dict = {}
        author_as_dict["name"] = self.name

        return author_as_dict

    @classmethod
    def from_dict(cls, author_data):  # POST/CREATE
        new_author = Author(name=author_data["title"],
                            description=author_data["description"])
        return author_data
