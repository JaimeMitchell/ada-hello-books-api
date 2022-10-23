from flask import Blueprint, jsonify


class Book:
    def __init__(self, id, title, author):
        self.id = id
        self.title = title
        self.author = author


books = [
    Book(1, "a title 1", "someone 1"),
    Book(2, "a title 2", "someone 2"),
    Book(3, "a title 3", "someone 3")
]

books_bp = Blueprint("books", __name__, url_prefix="/books")


@books_bp.route("", methods=["GET"])
def handle_all_books():
    books_response = []
    for book in books:
        books_response.append({
            "id": book.id,
            "title": book.title,
            "author": book.author
        })
    return jsonify(books_response)


@books_bp.route("<book_id>", methods=["GET"])
def handle_single_book(book_id):
    try:
        book_id == int(book_id)
    except:
        return f"{book_id} is invalid", 400
    for book in books:
        if book.id == book_id:
            return {
                "id": book.id,
                "title": book.title,
                "author": book.author
            }
    return f"{book_id} is non existant, so you're getting a 404"
