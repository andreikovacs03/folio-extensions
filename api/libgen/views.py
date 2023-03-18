from libgen_api import LibgenSearch
from flask import Blueprint

blueprint = Blueprint("libgen", __name__, url_prefix="/libgen")


@blueprint.route("/search_title/<title>")
def search_title(title: str):
    search = LibgenSearch()
    return search.search_title(title)
