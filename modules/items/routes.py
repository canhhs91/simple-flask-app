from flask import Blueprint
from .controllers import all, put, get

blueprint = Blueprint('item', __name__)

blueprint.route('/', methods=['GET'])(all)
blueprint.route('/', methods=['PUT'])(put)
blueprint.route('/<int:id>', methods=['GET'])(get)
