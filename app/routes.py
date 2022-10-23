
from flask import Blueprint, jsonify
# jsonify is a Flask utility function that turns its argument into JSON. We'll use jsonify as a way to turn a list of book dictionaries into a Response object.

hello_world_bp = Blueprint("hello_world_bp", __name__)


@hello_world_bp.route("/hello-world", methods=["GET"])
def say_hello_world():
    return "Hello, World!"


@hello_world_bp.route("/hello/JSON", methods=["GET"])
def say_hello_json():
    return {
        "name": "Ada Lovelace",
        "message": "Hello!",
        "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
    }


@hello_world_bp.route("/broken-endpoint-with-broken-server-code")
def broken_endpoint():
    response_body = {
        "name": "Ada Lovelace",
        "message": "Hello!",
        "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
    }
    new_hobby = "Surfing"
    response_body["hobbies"].append(new_hobby)
    return response_body

# Book class to represent hardcoded book data


class Book:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description


# List of instances of the Book class that serve that as hardcoded data
books = [
    Book(1, "kite making", "a books about string management"),
    Book(2, "picture of dorian gray", "victorian lgbt social commentary, youth fixation"),
    Book(3, "coffee", "i need some right now")
]

# Our Blueprint instance. We'll use it to group routes that start with /books. "books" is the debugging name for this Blueprint. __name__ provides information the blueprint uses for certain aspects of routing. We should use this blueprint for all of our RESTful routes that start with /books!
books_bp = Blueprint("books", __name__, url_prefix="/books")

# A decorator that uses the books_bp Blueprint to define an endpoint and accepted HTTP method. The following function will execute whenever a matching HTTP request is received.


@books_bp.route("", methods=["GET"])
# This function will execute whenever a request that matches the decorator is received. The name of this function doesn't affect how requests are routed to this method. Common choices for a function name could include matching the route path, or using any other good, descriptive Python function name.
def handle_books():
    books_response = []
    for book in books:
        books_response.append({
            "id": book.id,
            "title": book.title,
            "desciption": book.description
        })
    return jsonify(books_response)  # Can I return this without jsonify


