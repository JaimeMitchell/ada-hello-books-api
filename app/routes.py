from app import db
from app.models.book import Book
from flask import Blueprint, jsonify, make_response, request

books_bp = Blueprint("books", __name__, url_prefix="/books")


@books_bp.route("", methods=["GET", "POST"])
def handle_books():
    if request.method == "GET":
        books = Book.query.all()
        books_response = []
        for book in books:
            books_response.append({
                "id": book.id,
                "title": book.title,
                "description": book.description
            })
        return jsonify(books_response)
    elif request.method == "POST":
        # ... Indent all of the Create Book functionality into this elif
        request_body = request.get_json()
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
