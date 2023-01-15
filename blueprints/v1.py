from http import HTTPStatus

from flask import Blueprint
from flask import make_response
from flask import request
from flask_expects_json import expects_json
from webpreview import webpreview

from cache.methods import get_from_cache, set_to_cache

v1_blueprint = Blueprint('v1_blueprint', __name__)

basic_payload_schema = {
    "type": "object",
    "properties": {
        "link": {"type": "string"}
    },
    "required": ["link"]
}


@v1_blueprint.route('/', methods=['POST'])
@expects_json(basic_payload_schema)
def link_preview_api_v1():
    """
    v1 API definition is to provide title, description, image and url. Minimal opengraph definition.

    :arg:
        It is expected to have the link key in request object.

    :return:
        response object containing title, description, image and url along with the http code.
    """

    request_obj = request.get_json()
    link = request_obj['link']
    print('processing link preview for {0}'.format(link))

    # check if data is present in the cache first before calling the link previewer.
    response_data = get_from_cache(link)

    if response_data is None:
        """
        Call the link preview API and also store the results in cache.
        """
        p = webpreview(request_obj['link'])
        response_data = build_preview_response(p)
        set_to_cache(link, response_data)

    return make_response(response_data, HTTPStatus.OK)


def build_preview_response(p):
    response_data = {
        'title': p.title,
        'description': p.description,
        'image': p.image,
        'url': p.url
    }
    return response_data
