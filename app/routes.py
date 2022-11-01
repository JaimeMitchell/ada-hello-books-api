from app import db
from app.models.book import Book
from flask import Blueprint, jsonify, make_response, request, abort, make_response

books_bp = Blueprint("books_bp", __name__, url_prefix="/books")

# CREATE
@books_bp.route("", strict_slashes=False, methods=["POST"])
def create_book():
    request_body = request.get_json()
    new_book = Book(title=request_body["title"],
                    description=request_body["description"])

    db.session.add(new_book)
    db.session.commit()

    return make_response(f"Book {new_book.title} successfully created", 201)

# READ (GET ALL)
@books_bp.route("", strict_slashes=False, methods=["GET"])
def read_all_books():
    books_response = []
    books = Book.query.all()
    for book in books:
        books_response.append(
            {
                "id": book.id,
                "title": book.title,
                "description": book.description
            }
        )
    return jsonify(books_response)

#VALIDATE ID FOR GET ONE BOOK
def validate_book(book_id):
    try:
        book_id = int(book_id)
    except:
        abort(make_response({"message": f"book {book_id} invalid"}, 400))

    book = Book.query.get(book_id)

    if not book:
        abort(make_response({"message": f"book {book_id} not found"}, 404))

    return book

# READ (GET ONE)
@books_bp.route("/<book_id>", methods=["GET"])
def read_one_book(book_id):
    book = validate_book(book_id)
    return {
        "id": book.id,
        "title": book.title,
        "description": book.description
    }

# UPDATE (PUT)
@books_bp.route("/<book_id>", methods=["PUT"])
def update_book(book_id):
    book = validate_book(book_id)

    request_body = request.get_json() #`parse json into python dictionary

    book.title = request_body["title"]
    book.description = request_body["description"]

    db.session.commit()

    return make_response(f"Book #{book.id} successfully updated")