from flask import Flask


def create_app(test_config=None): #WHAT IS TEST_CONFIG = NONE
    app = Flask(__name__)

    from.routes import hello_world_bp
    app.register_blueprint(hello_world_bp)

    return app


