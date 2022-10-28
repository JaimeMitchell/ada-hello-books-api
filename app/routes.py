from flask import Blueprint, jsonify, abort, make_response

from flask import Blueprint

books_bp = Blueprint("books", __name__, url_prefix="/books") 

# @books_bp.route("", methods=["GET"]) 
# def handle_all_books():
#     books_response = []
#     for book in books:
#         books_response.append({
#             "id": book.id,
#             "title": book.title,
#             "description": book.description
#         })
#     return jsonify(books_response), 200


# def validate(book_id):
#     try:
#         book_id = int(book_id) 
#     except:
#         abort(make_response({"message": f"book {book_id} is invalid"}, 400))
#     for book in books:
#         if book.id == book_id:
#             return(book)
#     abort(make_response({"message": f"book {book_id} is non existant"}, 404))


# @books_bp.route("/<book_id>", methods=['GET'])
# def handle_book(book_id):
#     book = validate(book_id)
#     return{
#         "id": book.id,
#         "title": book.title,
#         "description": book.description
#     } 
