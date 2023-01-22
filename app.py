from http import HTTPStatus

from flask import Flask
from flask import make_response
from flask_cors import CORS

from blueprints.v1 import v1_blueprint


def create_app():
    _app = Flask(__name__)
    CORS(_app)

    @_app.route('/are_you_alive')
    def are_you_alive():
        return make_response({"message": "Hello from Link service"}, HTTPStatus.OK)

    @_app.errorhandler(500)
    def internal_server_error(error):
        return make_response({"message": error.description}, HTTPStatus.INTERNAL_SERVER_ERROR)

    @_app.errorhandler(404)
    def not_found_error(error):
        return make_response({"message": error.description}, HTTPStatus.NOT_FOUND)

    # resister the blueprints.
    _app.register_blueprint(v1_blueprint, url_prefix='/link-service/v1')

    return _app


if __name__ == "__main__":
    app = create_app()
    app.run()
