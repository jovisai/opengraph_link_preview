from http import HTTPStatus

from flask import Flask, jsonify
from flask import make_response
from flask_cors import CORS

from blueprints.v1 import v1_blueprint


def create_app():
    _app = Flask(__name__)
    CORS(_app)

    @_app.route('/are_you_alive')
    def are_you_alive():
        return make_response(jsonify({"msg": "Hello from Link service"}), HTTPStatus.OK)

    # resister the blueprints.
    _app.register_blueprint(v1_blueprint, url_prefix='/v1')

    return _app


if __name__ == "__main__":
    app = create_app()
    app.run()
