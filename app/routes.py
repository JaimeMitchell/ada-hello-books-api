from flask import Blueprint, jsonify


class Book:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description


books = [
    Book(1, "kite making", "a books about string management"),
    Book(2, "picture of dorian gray",
         "victorian lgbt social commentary, youth fixation"),
    Book(3, "coffee", "i need some right now")
]

books_bp = Blueprint("books", __name__, url_prefix="/books")


@books_bp.route("", methods=["GET"])
def handle_all_books():
    books_response = []
    for book in books:
        books_response.append({
            "id": book.id,
            "title": book.title,
            "description": book.description
        })
    return jsonify(books_response), 200


@books_bp.route("/<book_id>", methods=["GET"])
def handle_single_book(book_id):
    if book_id.isnumeric():
        book_id = int(book_id)
    for book in books:
        if book.id == book_id or book.title == book_id:
            return {
                "id": book.id,
                "title": book.title,
                "description": book.description}
    return {"message": f"{book_id} is non existant, so you're getting a 404"}, 404


@books_bp.route("/<book_id>", methods=['GET'])
def handle_book(book_id):
    if book_id.isnumeric():
        book_id = int(book_id)
    for book in books:
        if book.id == book_id or book.title == book_id:
            return{
                "id": book.id,
                "title": book.title,
                "description": book.description
            }
