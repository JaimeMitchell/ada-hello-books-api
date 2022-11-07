from app import db
from app.models.author import Author
from app.models.book import Book
from flask import Blueprint, jsonify, abort, make_response, request

authors_bp = Blueprint("authors_bp", __name__, url_prefix="/authors")


def validate_model(author_id):
    try:
        author_id = int(author_id)
    except:
        abort(make_response(
            jsonify({"message": f"Author {author_id} invalid"}, 400)))

    author = Author.query.get(author.id)

    if not author:
        abort(make_response(
            jsonify({"message": f"Author {author_id} not found"}, 404)))

    return author


@authors_bp.route("", methods=["POST"])
def create_author():
    request_body = request.get_json()
    new_author = Author(name=request_body["name"])
    db.session.add(new_author)
    db.session.commit()
    return jsonify(new_author.to_dict())


@authors_bp.route("/<author_id>/books", methods=["POST"])
def create_book(author_id):

    author = validate_model(Author, author_id)

    request_body = request.get_json()
    new_book = Book(title=request_body["title"],
                    description=request_body["description"],
                    author=author
                    )
    db.session.add(new_book)
    db.session.commit()
    return make_response(jsonify(f"Book {new_book.title} by {new_book.author.name} successfully created"), 201)


@authors_bp.route("", methods=["GET"])
def get_all_authors():

    name_query = request.args.get("name")
    if name_query:
        authors = Author.query.filter_by(name=name_query)
    else:
        authors = Author.query.all()

    authors_response = []
    for author in authors:
        authors_response.append(author.to_dict())
    return jsonify(authors_response)


@authors_bp.route("/<author_id>/books", methods=["GET"])
def read_books(author_id):

    author = validate_model(Author, author_id)

    books_response = []
    for book in author.books:
        books_response.append(
            {
                "id": book.id,
                "title": book.title,
                "description": book.description
            }
        )
    return jsonify(books_response)
