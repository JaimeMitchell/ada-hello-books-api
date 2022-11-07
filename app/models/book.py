from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id')) #FOREIGN KEY
    author = db.relationship("Author", back_populates="books")
    #THE MANY, CHILD (both have db.relationship, but only child has db.ForeignKey)

    def to_dict(self): #GET/READ
        book_as_dict = {}
        book_as_dict["id"] = self.id
        book_as_dict["title"] = self.title
        book_as_dict["description"] = self.description
        book_as_dict["author"] = self.author.to_dict()
        
        return book_as_dict

    @classmethod
    def from_dict(cls, book_data): #POST/CREATE
        new_book = Book(title=book_data["title"],
                        description=book_data["description"])
        return new_book