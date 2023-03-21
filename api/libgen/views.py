import urllib.parse
from libgen_api import LibgenSearch
from flask import Blueprint, request

blueprint = Blueprint("libgen", __name__, url_prefix="/libgen")


@blueprint.route("/search_title/<title>")
def search_title(title: str):
    s = LibgenSearch()
    return s.search_title(title)


@blueprint.route("/search_title_filtered/<title>", methods=["POST"])
def search_title_filtered(title: str):
    s = LibgenSearch()
    filters = request.get_json()
    return s.search_title_filtered(title, filters, exact_match=True)


@blueprint.route("/download/<link>")
def download(link: str):
    s = LibgenSearch()
    decoded_link = urllib.parse.unquote(link)
    return s.resolve_download_links({"Mirror_1": decoded_link})
