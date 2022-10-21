from flask import Flask
app = Flask(__name__)


@app.route('/Syrup/')  # Tells Flask what URL will trigger our function
def hello_world():
    return 'Hello World'
